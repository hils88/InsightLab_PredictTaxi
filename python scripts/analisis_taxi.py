import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split, cross_val_score
from sklearn.preprocessing import StandardScaler, OneHotEncoder
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_squared_error, mean_absolute_error, r2_score
import joblib
import warnings
warnings.filterwarnings("ignore")

class AnalisisTaxi:
    def __init__(self):
        # Data y pipeline
        self.df = None
        self.model = None
        self.preprocessor = None

        # Train/test
        self.X_train = self.X_test = self.y_train = self.y_test = None

        # Features
        self.num_features = []
        self.cat_features = []

    # Carga de datos
    #Carga CSV y normaliza nombres comunes del dataset NYC Yellow Taxi
    def cargar_datos(self, archivo_csv: str, nrows: int = None):
        
        df = pd.read_csv(archivo_csv, nrows=nrows)
        col_map = {}
        for c in ['tpep_pickup_datetime', 'pickup_datetime']:
            if c in df.columns:
                col_map[c] = 'pickup_datetime'
                break
        for c in ['tpep_dropoff_datetime', 'dropoff_datetime']:
            if c in df.columns:
                col_map[c] = 'dropoff_datetime'
                break
        for c in ['PULocationID', 'pickup_location_id', 'PUlocationID', 'pu_location_id']:
            if c in df.columns:
                col_map[c] = 'pickup_location_id'
                break
        for c in ['DOLocationID', 'dropoff_location_id', 'DOlocationID', 'do_location_id']:
            if c in df.columns:
                col_map[c] = 'dropoff_location_id'
                break
        for c in ['trip_distance', 'Trip_distance']:
            if c in df.columns:
                col_map[c] = 'trip_distance'
                break
        for c in ['fare_amount', 'Fare_amount', 'fare']:
            if c in df.columns:
                col_map[c] = 'fare_amount'
                break

        self.df = df.rename(columns=col_map)
        print(f"[info] Archivo cargado. Registros: {len(self.df)}")

    # Limpieza
    # Parsea datetimes, crea duration_minutes y campos extras
    def limpiar(self):
        
        if self.df is None:
            raise ValueError("Carga los datos primero con .cargar_datos()")

        df = self.df.copy()

        
        if 'pickup_datetime' in df.columns:
            df['pickup_datetime'] = pd.to_datetime(df['pickup_datetime'], errors='coerce')
        if 'dropoff_datetime' in df.columns:
            df['dropoff_datetime'] = pd.to_datetime(df['dropoff_datetime'], errors='coerce')

        
        if 'pickup_datetime' in df.columns and 'dropoff_datetime' in df.columns:
            df['duration_minutes'] = (df['dropoff_datetime'] - df['pickup_datetime']).dt.total_seconds() / 60.0
        else:
            df['duration_minutes'] = np.nan

        
        if 'pickup_datetime' in df.columns:
            df['pickup_hour'] = df['pickup_datetime'].dt.hour
            df['pickup_dow'] = df['pickup_datetime'].dt.dayofweek  # 0 = Mon
            df['is_weekend'] = df['pickup_dow'].isin([5, 6]).astype(int)
            df['is_peak'] = df['pickup_hour'].apply(lambda h: 1 if (7 <= h <= 9) or (16 <= h <= 19) else 0)
        else:
            df['pickup_hour'] = np.nan
            df['pickup_dow'] = np.nan
            df['is_weekend'] = 0
            df['is_peak'] = 0

        
        df['trip_distance'] = pd.to_numeric(df.get('trip_distance', pd.Series(np.nan)), errors='coerce')
        df['fare_amount'] = pd.to_numeric(df.get('fare_amount', pd.Series(np.nan)), errors='coerce')

        
        for c in ['pickup_location_id', 'dropoff_location_id']:
            if c in df.columns:
                df[c] = df[c].astype(str)
            else:
                df[c] = 'unk'

        self.df = df
        print(f"[info] Limpieza completada. Registros: {len(self.df)}")
    
    #filtrar datos que no hagan sentido
    def filtrar_outliers(self,
                        min_duration=0.5, max_duration=600,
                        min_distance=0.01, max_distance=500,
                        min_fare=0):

        if self.df is None:
            raise ValueError("Carga y procesa datos primero")

        df = self.df.copy()
        if 'duration_minutes' in df.columns:
            df = df[df['duration_minutes'].notnull()]
            df = df[(df['duration_minutes'] >= min_duration) & (df['duration_minutes'] <= max_duration)]
        df = df[df['trip_distance'].notnull()]
        df = df[(df['trip_distance'] >= min_distance) & (df['trip_distance'] <= max_distance)]
        df = df[df['fare_amount'].notnull()]
        df = df[df['fare_amount'] >= min_fare]
        df = df.dropna(subset=['pickup_datetime', 'trip_distance'])
        self.df = df.reset_index(drop=True)
        print(f"[info] Outliers filtrados. Registros restantes: {len(self.df)}")

    # Preparar train/test
    #  Prepara X,y y realiza train/test split. Target: 'duration_minutes' o 'fare_amount'
      
    def preparar_train_test(self, target: str = 'duration_minutes', test_size: float = 0.2, random_state: int = 42, sample_frac: float = None):
       
        if self.df is None:
            raise ValueError("Carga y procesa datos primero")

        df = self.df.copy()
        if sample_frac is not None and 0 < sample_frac < 1:
            df = df.sample(frac=sample_frac, random_state=random_state).reset_index(drop=True)

        if target not in df.columns:
            raise ValueError(f"Target {target} no encontrado en dataframe")

        # Features simples elegidas por rendimiento y disponibilidad
        X = df[['trip_distance', 'pickup_hour', 'pickup_dow', 'is_weekend', 'is_peak', 'pickup_location_id', 'dropoff_location_id']].copy()
        y = df[target].copy()

        # listas de features
        self.num_features = ['trip_distance', 'pickup_hour', 'pickup_dow', 'is_weekend', 'is_peak']
        self.cat_features = ['pickup_location_id', 'dropoff_location_id']

        # split
        X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=test_size, random_state=random_state)
        self.X_train, self.X_test, self.y_train, self.y_test = X_train, X_test, y_train, y_test
        print(f"[info] Train/Test preparados. Train: {X_train.shape}, Test: {X_test.shape}")

    # Pipeline con Random Forest
    #Crea pipeline con StandardScaler + OneHotEncoder + RandomForestRegressor
    def crear_pipeline_random_forest(self, n_estimators: int = 100, max_depth: int = None, min_samples_leaf: int = 1):
       
        if not self.num_features and not self.cat_features:
            raise ValueError("Ejecuta preparar_train_test() antes de crear pipeline")
   
        try:
            encoder = OneHotEncoder(handle_unknown='ignore', sparse_output=False)
        except TypeError:
            encoder = OneHotEncoder(handle_unknown='ignore', sparse=False)

        preprocessor = ColumnTransformer(transformers=[
            ('num', StandardScaler(), self.num_features),
            ('cat', encoder, self.cat_features)
        ], remainder='drop')

        rf = RandomForestRegressor(n_estimators=n_estimators, max_depth=max_depth, min_samples_leaf=min_samples_leaf,n_jobs=-1, random_state=42)

        pipeline = Pipeline(steps=[
            ('preproc', preprocessor),
            ('rf', rf)
        ])

        self.model = pipeline
        self.preprocessor = preprocessor
        print(f"[info] Pipeline creado con RandomForest (n_estimators={n_estimators}, max_depth={max_depth}, min_samples_leaf={min_samples_leaf})")

     #entrenar modelo para costo basado en fare_amount 
    def crear_pipeline_random_forest_costo(self, n_estimators: int = 100, max_depth: int = None, min_samples_leaf: int = 1):

        if not self.num_features and not self.cat_features:
            raise ValueError("Ejecuta preparar_train_test() antes de crear pipeline")
        
        try:
            encoder = OneHotEncoder(handle_unknown='ignore', sparse_output=False)
        except TypeError:
            encoder = OneHotEncoder(handle_unknown='ignore', sparse=False)

        preprocessor = ColumnTransformer(transformers=[
            ('num', StandardScaler(), self.num_features),
            ('cat', encoder, self.cat_features)
        ], remainder='drop')

        rf = RandomForestRegressor(
            n_estimators=n_estimators,
            max_depth=max_depth,
            min_samples_leaf=min_samples_leaf,
            n_jobs=-1,
            random_state=42
        )

        pipeline = Pipeline(steps=[
            ('preproc', preprocessor),
            ('rf', rf)
        ])

        self.model_costo = pipeline
        self.preprocessor_costo = preprocessor

        # Definir X y y para costo
        X = self.df[self.num_features + self.cat_features]
        y = self.df['fare_amount']

        # Dividir train/test
        self.X_train_costo, self.X_test_costo, self.y_train_costo, self.y_test_costo = train_test_split(
            X, y, test_size=0.3, random_state=42
        )

        # Entrenar modelo
        self.model_costo.fit(self.X_train_costo, self.y_train_costo)
        print(f"[info] Pipeline Random Forest creado y entrenado para costo (n_estimators={n_estimators}, max_depth={max_depth}, min_samples_leaf={min_samples_leaf})")


        # Entrenamiento y evaluacion
    def entrenar(self):
       
        if self.model is None:
            raise ValueError("Crea pipeline primero con crear_pipeline_random_forest()")
        self.model.fit(self.X_train, self.y_train)
        print("[info] Modelo entrenado.")

    def evaluar(self):
      
        if self.model is None:
            raise ValueError("Entrena el modelo primero")
        y_pred = self.model.predict(self.X_test)
        mse = mean_squared_error(self.y_test, y_pred)
        rmse = np.sqrt(mse)
        mae = mean_absolute_error(self.y_test, y_pred)
        r2 = r2_score(self.y_test, y_pred)
        metrics = {'rmse': rmse, 'mae': mae, 'r2': r2}
        print("[info] Evaluación del modelo ->", metrics)
        return metrics

    def validacion_cruzada(self, cv: int = 5):
       
        if self.model is None:
            raise ValueError("Crea pipeline primero")
        scores = cross_val_score(self.model, self.X_train, self.y_train, cv=cv, scoring='r2', n_jobs=-1)
        print(f"[info] Cross-val R2 (mean): {scores.mean():.3f}, std: {scores.std():.3f}")
        return scores
    
    # Predecir una fila para tiempo

    def predecir_fila(self, fila: dict):

        if self.model is None:
            raise ValueError("Carga o entrena un modelo primero")
        X_row = pd.DataFrame([fila])
        pred = self.model.predict(X_row)[0]
        return float(pred)
    
    # predecir una fila para costo
    def predecir_fila_costo(self, fila: dict):
        """        fila: dict con keys ['trip_distance','pickup_hour','pickup_dow','is_weekend',
                            'is_peak','pickup_location_id','dropoff_location_id']
        """
        if self.model_costo is None:
            raise ValueError("Carga o entrena primero el modelo de costo")
        
        # Convertir fila a DataFrame
        X_row = pd.DataFrame([fila])
        
        # Predicción
        pred_costo = self.model_costo.predict(self.preprocessor_costo.transform(X_row))[0]
        
        return float(pred_costo)

    

