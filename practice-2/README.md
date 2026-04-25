# Práctica 2 — Aprendizaje No Supervisado

Este directorio contiene la **Práctica 2** de la asignatura **Aprendizaje Automático**, desarrollada en un único cuaderno Jupyter/Colab.

## Autor
- **Nombre:** Ismael Sallami Moreno

## Contenido del proyecto
- `P2_Sallami_Moreno_Ismael.ipynb`: cuaderno principal con toda la práctica.

## Descripción general de la práctica
La práctica está dividida en **dos ejercicios principales**:

### 1) Agrupamiento / Clustering (5 puntos)
Se aborda la segmentación de clientes de un centro comercial utilizando variables de ingreso anual y puntuación de gasto.

Flujo seguido:
- Carga y exploración inicial del dataset de clientes.
- EDA con histogramas, boxplots y análisis bivariante.
- Estandarización de variables con `StandardScaler`.
- Selección de `k` en K-Means mediante Método del Codo y validación con Silueta.
- Entrenamiento de K-Means e interpretación de segmentos.
- Entrenamiento de DBSCAN con ajuste de `eps` y `min_samples` (incluyendo k-distance plot).
- Comparativa visual K-Means vs DBSCAN.
- Análisis extra con dendrograma (clustering jerárquico) como validación adicional.

Resultados destacados:
- K-Means se valida con **k = 5**.
- DBSCAN identifica **6 clústeres** y detecta **23 observaciones de ruido**.

### 2) Reglas de Asociación (5 puntos)
Se realiza análisis de cesta de la compra (*Market Basket Analysis*) para descubrir patrones de co-compra.

Flujo seguido:
- Carga y transformación de transacciones con `TransactionEncoder`.
- Minería de itemsets frecuentes y reglas de asociación.
- Evaluación de métricas de calidad (soporte, confianza y *lift*).
- Comparativa algorítmica entre:
  - Apriori
  - FP-Growth
  - FP-Max
  - H-Mine (si está disponible en la versión instalada)
- Benchmarking de tiempos e interpretación comercial de reglas.

Resultados destacados:
- Apriori, FP-Growth y H-Mine convergen en **333 itemsets**.
- FP-Max devuelve **243 itemsets** (filtrado de subconjuntos al extraer itemsets maximales).
- Regla principal reportada: `{yogurt, whole milk} -> {curd}` con *lift* aproximado **3.37**.

## Librerías utilizadas
- `pandas`
- `numpy`
- `matplotlib`
- `seaborn`
- `scikit-learn`
- `scipy`
- `mlxtend`
- `time`
- `warnings`

## Cómo ejecutar
### Opción A: Google Colab
1. Abrir `P2_Sallami_Moreno_Ismael.ipynb` en Colab.
2. Ejecutar todas las celdas en orden (`Entorno de ejecución` -> `Ejecutar todo`).

### Opción B: Jupyter en local
1. Crear/activar entorno virtual (opcional, recomendado).
2. Instalar dependencias:
   ```bash
   pip install pandas numpy matplotlib seaborn scikit-learn scipy mlxtend jupyter
   ```
3. Lanzar Jupyter:
   ```bash
   jupyter notebook
   ```
4. Abrir `P2_Sallami_Moreno_Ismael.ipynb` y ejecutar las celdas en orden.

## Notas
- El notebook incluye documentación extensa de las decisiones metodológicas y la interpretación de resultados.
- Los datasets se cargan desde URLs públicas, por lo que se requiere conexión a Internet para una ejecución completa.
- En algunas ejecuciones pueden aparecer *warnings* de dependencias de Jupyter/Colab que no afectan al desarrollo de la práctica.
