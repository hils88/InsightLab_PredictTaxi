# InsightLab_PredictTaxi

Proyecto que predice la duración de viajes en taxi utilizando datos reales, tecnicas de analisis y modelos de machine learning. Este proyecto es importante porque ayuda a optimizar rutas y mejorar la planificacion del transporte urbano.

![Python](https://img.shields.io/badge/Python-3.13-blue)
![License](https://img.shields.io/badge/License-MIT-green)
![Status](https://img.shields.io/badge/Status-Completed-brightgreen)
![pandas](https://img.shields.io/badge/pandas-2.3.1-blue)
![scikit-learn](https://img.shields.io/badge/scikit--learn-1.7.2-orange)
![Random Forest](https://img.shields.io/badge/Model-Random%20Forest-brightgreen)

## Problema que se resuelve

Los pasajeros y conductores de taxis pierden tiempo diariamente debido a predicciones inexactas de la duracion de los viajes. Los metodos tradicionales basados en estimaciones promedio no capturan la variabilidad del trafico ni la hora del día, lo que resulta en retrasos frecuentes y rutas ineficientes, generando perdida de tiempo en los recorridos diarios.

## Solucion propuesta

Se desarrollo un sistema de prediccion de la duracion de viajes en taxi que analiza datos historicos de viajes, considerando distancia, hora de recogida, ubicacion de origen y destino. Utiliza tecnicas de análisis de datos y un modelo de **Random Forest** para generar predicciones precisas del tiempo de viaje. El proyecto produce **estimaciones de duración para cada viaje**, patrones de trafico y metricas de desempeño del modelo, ayudando a optimizar rutas, reducir retrasos y mejorar la eficiencia del servicio.

## Caracteristicas principales

- Prediccion de la duracion de viajes en taxi utilizando **Random Forest**.  
- Analisis de datos historicos de viajes (distancia, hora, ubicación de origen y destino).  
- Comparacion de predicciones vs valores vecinos
- Estimaciones precisas para optimizar rutas y reducir retrasos.  
- Metricas de desempeño del modelo para evaluar precision y confiabilidad.  
- Herramienta util para conductores y empresas de transporte urbano para mejorar eficiencia y planificacion.

## Tecnologías y librerías

- **Python 3.13** – Lenguaje principal del proyecto.  
- **pandas** – Manipulación y limpieza de datos.  
- **scikit-learn** – Modelos de machine learning, incluyendo **Random Forest**.  
- **matplotlib** – Visualizacion de datos en gráficos estáticos.  
- **seaborn** – Visualizacion y análisis de patrones.  
- **Jupyter Notebook / Visual Studio Code** – Entorno para desarrollo y pruebas del modelo.

## Estructura del proyecto
```
InsightLab_PredictTaxi
├── data
│ └── yellow_tripdata_2016-03.csv #archivo con datos fuentes
├── docs - bitacoras
│ └── bitacora 1 #bitacora de trabajo con design thinking
│ └── bitacora 2 #bitacora de trabajo con git y github
├── notebooks
│ └── taxi_prediction.ipynb #notebook de trabajo
├── python_scripts
│ └── analisis_taxi.py #script que contiene todas las funciones a utilizar para la prediccion
├── .gitignore
├── LICENSE
└── README.md
```
## Instalacion y uso

### Prerrequisitos
Antes de ejecutar el proyecto, asegurate de tener instalado:
- **Python 3.13** o superior
- **pip** (gestor de paquetes de Python)
- Un editor de codigo o IDE como **Jupyter Notebook**, **VS Code**

### Pasos de instalacion

1. Clonar el repositorio:

```bash
git clone https://github.com/tuusuario/InsightLab_PredictTaxi.git
```
2. Acceder a la carpeta del proyecto:
   ```bash
   cd InsightLab_PredictTaxi
   ```
3. Instalar las librerias necesarias: pip install pandas scikit-learn matplotlib seaborn

### Uso

1. Abrir el notebook principal para análisis y predicción
```bash
jupyter notebook notebooks/taxi_prediction.ipynb
```
## Resultados

### Evaluacion del modelo

<p align="center">
  <img src="img - resultados/evaluacion_de_modelo.png" alt="Evaluacion de modelo" width="500"/>
</p>

El modelo se entreno utilizando 200,000 registros del dataset de taxis, con el objetivo de predecir el tiempo total de viaje. Las metricas de evaluacion obtenidas son las siguientes:

RMSE: 4.87 minutos
Este valor indica que las predicciones del modelo presentan un desvio promedio de alrededor de 4.87 minutos respecto al tiempo real. Considerando la variabilidad natural del trafico urbano, este nivel de error es adecuado para tareas de estimación de tiempos de viaje

MAE: 3.39 minutos
El error absoluto promedio es de 3.39 minutos, lo cual refleja que el modelo mantiene un margen de error relativamente bajo en comparación con la duracion típica de los viajes. 

R2: 0.7528
El modelo logra explicar aproximadamente el 75% de la variacion total del tiempo de viaje. Este valor implica un buen ajuste, especialmente considerando que existen factores externos no incluidos en el dataset (congestion vial, clima, eventos locales) que afectan directamente la duracion de los viajes.

Como conclusion, los resultados demuestran que el modelo Random Forest ofrece un desempeño solido para la prediccion de tiempos de viaje. El nivel de error es consistente con modelos aplicados a entornos urbanos reales, y el valor de R2 confirma que el modelo captura de forma efectiva los patrones de movilidad presentes en los datos.

### Validacion cruzada

<p align="center">
  <img src="img - resultados/validacion_cruzada.png" alt="Validacion cruzada" width="500"/>
</p>

Para evaluar la estabilidad y capacidad de generalizacion del modelo Random Forest, se realizo una validación cruzada. Los resultados obtenidos para la metrica R2 fueron los siguientes:
Fold 1: 0.7452
Fold 2: 0.7495
Fold 3: 0.7473

A partir de estas evaluaciones se calcularon los valores estadisticos:
R2 promedio: 0.747
Desviacion estandar: 0.002

El valor promedio de R2 = 0.747 indica que el modelo explica alrededor del 74.7% de la variabilidad del tiempo de viaje de forma consistente. La desviacion estandar extremadamente baja (0.002) demuestra que el desempeño entre los diferentes folds es muy estable. Esta validación cruzada confirma que el modelo Random Forest esta bien ajustado y es robusto para predecir duraciones de viaje en datos no vistos

### Ejemplo de prediccion

Se realizo una prediccion con los siguientes datos:
Distancia: 3.2 millas
Hora del día: 3 p.m.
Dia de la semana: Jueves (pickup_dow = 4)
Fin de semana: No
Hora pico: Si (is_peak = 1)
Pickup zone: 237
Dropoff zone: 161

El modelo predijo una duracion estimada de 26.8 minutos

<p align="center">
  <img src="img - resultados/prediccion_ejemplo_1.png" alt="Prediccion de ejemplo 1" width="500"/>
</p>

En el primer grafico se ve que la mayoria de viajes duran entre 5 y 20 minutos pero tambien hay una cola larga de viajes de 25–40 minutos, dependiendo del trafico y la zona. La predicción marcada con la linea roja cerca de los 27 minutos, esta en una region donde si existen viajes reales solo que con menor frecuencia.
La duración predicha no está fuera del rango tipico

<p align="center">
  <img src="img - resultados/grafico_duracion_viajes.png" alt="Grafico de duracion de viajes" width="500"/>
</p>

En el segundo grafico se aprecia que distancias de 3 millas normalmente se asocian a duraciones entre 20 y 30 minutos y el punto de 3.2 millas cae en la tendencia.
<p align="center">
  <img src="img - resultados/grafico_prediccion_distancia.png" alt="Grafico de distancias" width="500"/>
</p>

Tambien se predijeron los siguientes viajes:

| trip_distance | pickup_hour | pickup_dow | is_weekend | is_peak | pickup_location_id | dropoff_location_id |
|---------------|-------------|------------|------------|---------|---------------------|----------------------|
| 3.2  | 15 | 4 | 0 | 1 | 237 | 161 |
| 7.5  | 9  | 2 | 0 | 1 | 100 | 230 |
| 1.8  | 22 | 5 | 1 | 0 | 50  | 12  |
| 12.0 | 8  | 1 | 0 | 1 | 45  | 90  |
| 5.5  | 18 | 6 | 1 | 1 | 210 | 55  |

<p align="center">
  <img src="img - resultados/prediccion_vecinos.png" alt="Prediccion de vecinos" width="500"/>
</p>

Viaje 1 – Distancia 3.2 mi, hora pico (15:00)
El modelo predice 26.8 min. La mediana de vecinos similares es 20.4 min, lo cual indica que la prediccion es ligeramente mas alta, posiblemente debido a la hora pico y zonas especificas de origen/destino analizadas por el modelo. Aun asi, se encuentra dentro de un rango razonable dado el comportamiento tipico de estos viajes.

Viaje 2 – Distancia 7.5 mi, mañana en hora pico (09:00)
Predicción de 27.96 min, muy alineada con la mediana historica de 26.38 min. Esto sugiere un buen ajuste del modelo para trayectos largos en horarios congestionados.

Viaje 3 – Distancia 1.8 mi, noche (22:00), fin de semana
El modelo predice 14.24 min, pero no se encontraron vecinos similares segun los criterios definidos. En este caso, la validacion externa no puede realizarse sin embargo la prediccion es coherente con la duracion tipica de viajes cortos en horarios nocturnos.

Viaje 4 – Distancia 12 mi, hora pico matutina (08:00)
El modelo predice un viaje largo: 43.11 min. La mediana historica de vecinos (38.03 min) respalda la idea de un trayecto extenso en condiciones de alto trafico. El modelo tiende a estimar ligeramente por encima, algo esperado en trayectos de larga distancia.

Viaje 5 – Distancia 5.5 mi, tarde noche fin de semana (18:00)
La prediccion es 30.10 min, mientras que los datos historicos muestran una mediana de 26.18 min. Nuevamente, la relacion es consistente y la diferencia probable se debe a factores como congestion variable o zonas especificas.

## Roadmap y Contribucion

### Versión actual (v1.0)
- Modelo basico de prediccion de duracion de viajes usando Random Forest  
- Visualizacion de resultados y patrones de trafico  
- API REST basica para consultar predicciones

### Proximas versiones
- Integracion de API de trafico en tiempo real  
- Integración de datos climaticos para mejorar la prediccion  
- Dashboard interactivo para visualizar predicciones y metricas  
- Optimizacion del modelo y nuevas metricas de desempeño  

### Como contribuir
Si quieres contribuir al proyecto:
1. Haz un **fork** del repositorio.  
2. Crea una nueva **branch** para tus cambios:  
   ```bash
   git checkout -b nombre-de-tu-branch
   ```
3. Realiza tus cambios y haz commit
   ```bash
   git commit -m "Descripción de tus cambios"
   ```
4. Haz push a tu branch
   ```bash
   git push origin nombre-de-tu-branch
   ```
5. Abre un Pull Request en el repositorio principal para revision

## Equipo y Contacto

**Autor:** Hilsia Hernandez  
**GitHub:** [https://github.com/hils88](https://github.com/hils88)  

**Licencia:**  
Este proyecto está bajo la licencia **MIT**. Para más detalles, consulta el archivo LICENSE.


