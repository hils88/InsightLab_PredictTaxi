# Project Charter: PredictTaxi – Prediccion de Duración de Viajes en NYC

## 1. Objetivo del negocio
El proyecto **PredictTaxi** busca resolver el problema de **incertidumbre en la duracion de viajes en taxi en Nueva York**, lo que afecta la planificacion de rutas, la satisfacción 
de los pasajeros y la eficiencia de los conductores.  
**Problema de negocio:** Las empresas de transporte y aplicaciones de movilidad pierden tiempo y recursos debido a estimaciones inexactas de duracion de viajes. 
Este proyecto permitira tomar decisiones mas informadas y mejorar la experiencia del usuario.

## 2. Objetivo de Data Science
Responder a la pregunta ¿Cual sera la duracion de un viaje en taxi en NYC dados los datos de origen, destino, hora, dia y condiciones externas?  

**Que se va a predecir:**  
- Duracion estimada de cada viaje en minutos.  
- Modelos de predicción basados en características como distancia, hora del día, día de la semana y ubicación de recogida/entrega.  

## 3. Alcance

**Incluye:**  
- Modelado de prediccion de tiempo de viaje usando Random Forest.  
- Analisis de tendencias históricas de viajes.  
- Visualizacion de resultados (gráficos y dashboards).  
- Manejo de datos de taxi de NYC históricos .

**No incluye:**  
- Datos en tiempo real (API de trafico o clima en esta version).  
- Prediccion de precios de viaje.  
- Integracion con apps de movilidad externas en esta fase.

## 4. Stakeholders
- **Product Owner:** gerente de Yellow Fleet NYC.  
- **Data Scientist:** Hilsia Hernandez.  
- **Usuarios finales:** Empresas de transporte, conductores de taxi, plataformas de movilidad.

## 5. Metricas de exito
- Precision del modelo.  
- Capacidad de generar predicciones para cualquier combinacion de pickup y dropoff de NYC.  
- Visualizacion clara de resultados y tendencias historicas.  
- Cumplimiento del timeline y entregables de MVP y version final.

## 6. Timeline
- **Inicio del proyecto:** 10/noviembre/2025  
- **Entrega MVP:** 17/noviembre/2025 – incluye modelo básico y visualizaciones iniciales  
- **Entrega final:** 5/enero/2026 – incluye mejoras en el modelo, dashboards completos y documentación

