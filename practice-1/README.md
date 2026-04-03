# Práctica 1 — Aprendizaje Supervisado

Este repositorio contiene la **Práctica 1** de la asignatura **Aprendizaje Automático**, desarrollada en un único cuaderno Jupyter/Colab.

## Autor
- **Nombre:** Ismael Sallami Moreno

## Contenido del proyecto
- `P1_Ismael_Sallami_Moreno.ipynb`: cuaderno principal con toda la práctica.

## Descripción general de la práctica
La práctica está dividida en **dos ejercicios principales**:

### 1) Problema de clasificación (5 puntos)
Se aborda la clasificación multiclase del rango de precio de teléfonos móviles (`price_range`) a partir de variables técnicas (RAM, batería, cámara, etc.).

Flujo seguido:
- Carga y exploración inicial del dataset.
- EDA con correlaciones y visualizaciones (heatmap, boxplots).
- Revisión de limpieza de datos (nulos y outliers, incluyendo verificación con IQR).
- Preprocesado: partición `train/test` y escalado con `StandardScaler`.
- Reducción/selección de características de baja correlación.
- Entrenamiento y comparación de varios modelos:
  - Regresión Logística
  - KNN
  - SVM
  - Random Forest
- Evaluación con métricas de clasificación multiclase:
  - `accuracy`
  - `classification_report` (precision/recall/F1 macro y weighted)
  - Matriz de confusión

### 2) Problema de regresión (5 puntos)
Se trabaja la predicción de la resistencia del hormigón (`strength`) a partir de sus componentes y condiciones.

Flujo seguido:
- Carga y análisis exploratorio del dataset de regresión.
- Análisis de correlaciones y distribución de la variable objetivo.
- Partición `train/test` y estandarización para evitar data leakage.
- Entrenamiento y comparación de modelos de regresión:
  - Regresión Lineal
  - SVR
  - KNN Regressor
  - Random Forest Regressor
- Evaluación con métricas de regresión:
  - `MAE`
  - `MSE`
  - `R²`

## Librerías utilizadas
- `pandas`
- `numpy`
- `matplotlib`
- `seaborn`
- `scikit-learn`

## Cómo ejecutar
### Opción A: Google Colab
1. Abrir `P1_Ismael_Sallami_Moreno.ipynb` en Colab.
2. Ejecutar todas las celdas en orden (`Entorno de ejecución` → `Ejecutar todo`).

### Opción B: Jupyter en local
1. Crear/activar entorno virtual (opcional, recomendado).
2. Instalar dependencias:
   ```bash
   pip install pandas numpy matplotlib seaborn scikit-learn jupyter
   ```
3. Lanzar Jupyter:
   ```bash
   jupyter notebook
   ```
4. Abrir `P1_Ismael_Sallami_Moreno.ipynb` y ejecutar las celdas en orden.

## Notas
- El notebook integra tanto el código como la justificación metodológica y teórica de las decisiones tomadas.
- Los datasets se cargan desde URLs públicas, por lo que se requiere conexión a Internet para una ejecución completa.
