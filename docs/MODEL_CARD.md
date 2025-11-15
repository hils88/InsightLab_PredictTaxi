# Model Card – PredictTaxi v1.0

## Descripcion del Modelo
El modelo **PredictTaxi v1.0** esta diseñado para predecir la **duración de los viajes en taxi en NYC**, usando datos historicos del mes de marzo de 2016. 
Permite a empresas de transporte y plataformas de movilidad estimar tiempos de viaje, mejorar la planificacion de rutas y optimizar la experiencia del usuario.

- **Algoritmo:** Random Forest Regressor  
- **Framework:** scikit-learn  
- **Fecha de Entrenamiento:** 12/noviembre/2025  

## Datos de Entrenamiento
- **Numero de registros:** 200,000. Despues de realizar limpieza y eliminar outliers: 196,607  
- **Periodo de los datos:** Marzo 2016  
- **Features utilizadas:** 14 (trip_distance, pickup_hour, pickup_dow, is_weekend, is_peak, pickup_location_id, dropoff_location_id, passenger_count, trip_type, payment_type, fare_amount, extra_charges, total_amount, pickup_datetime)  

## Performance del Modelo
| Metrica | Valor |
|----------|-------|
| RMSE     | 4.873298697549432 |
| MAE      | 3.39458903508923 |
| R²       | 0.752798606728114 |

## Limitaciones Conocidas
- El modelo fue entrenado con **datos históricos de un solo mes** (marzo 2016), por lo que puede no generalizar a otros periodos o cambios estacionales.  
- No incorpora información en tiempo real (trafico, clima).  
- La precision depende de la calidad y exactitud de los datos de origen y destino.

## Uso Recomendado
- Estimacion de duracion de viajes para analisis historico o planificacion aproximada de rutas.  
- No usar para decisiones criticas en tiempo real sin ajustar el modelo con datos mas recientes.  
- Ideal para integracion en dashboards internos de analisis y reportes de eficiencia en transporte.
