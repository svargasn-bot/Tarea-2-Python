# Análisis Exploratorio de Datos: Freelancers Globales

**Asignatura:** Taller de Python para Ciencia de Datos

## Integrantes
- Sebastian Vargas
- Sebastian Leon
- Rodrigo Ramirez

---

## Descripción del Proyecto

Este proyecto realiza un análisis completo de datos sobre freelancers a nivel global. Incluye:
- **Análisis Exploratorio de Datos (EDA)**: Exploración inicial del dataset
- **Preparación y Limpieza de Datos**: Normalización, estandarización e imputación de valores faltantes
- **Visualización de Datos**: Gráficos estadísticos y análisis de correlaciones

El objetivo es identificar patrones, tendencias y relaciones en el comportamiento de freelancers en diferentes geografías, idiomas, habilidades y tasas horarias.

---

## Estructura del Proyecto

```
Tarea-2-Python/
├── README.md                                 # Este archivo
├── data/
│   ├── raw/
│   │   └── global_freelancers_raw.csv       # Datos originales sin procesar
│   └── processed/
│       └── global_freelancers_processed.csv # Datos limpios y procesados
├── notebooks/
│   ├── 01_eda.ipynb                         # Análisis Exploratorio de Datos
│   ├── 02_preparation.ipynb                 # Preparación y Limpieza de Datos
│   └── 03_visualization.ipynb               # Visualizaciones y Gráficos
├── src/
│   ├── __init__.py                          # Inicializador del paquete
│   ├── preparation.py                       # Funciones de limpieza y preparación
│   └── plots.py                             # Funciones para generar gráficos
└── outputs/
    └── figures/                             # Gráficos generados
```

---

## Flujo de Trabajo

### 1. **Preparación de Datos** (`02_preparation.ipynb`)
Se realizan las siguientes transformaciones:
- Limpieza de espacios en blanco en nombres de columnas
- **Normalización de género**: Unificación de variantes (f/female/fem → Female; m/male/masc → Male)
- **Estandarización de estado activo**: Conversión de valores booleanos inconsistentes
- **Limpieza de datos numéricos**:
  - Remoción de símbolos de moneda ($, USD)
  - Conversión de porcentajes a valores numéricos
- **Imputación de valores faltantes**: Reemplazo con medianas de variables numéricas

**Entrada:** `data/raw/global_freelancers_raw.csv`  
**Salida:** `data/processed/global_freelancers_processed.csv`

### 2. **Análisis Exploratorio** (`01_eda.ipynb`)
- Visualización de estructura del dataset (dimensiones, tipos de datos)
- Estadísticas descriptivas generales
- Identificación de valores faltantes
- Análisis de frecuencias en variables categóricas

### 3. **Visualización** (`03_visualization.ipynb`)
Genera los siguientes gráficos:
- **Histograma de Edades**: Distribución de edades de los freelancers
- **Gráfico de Torta (Idiomas)**: Distribución de lenguajes principales
- **Matriz de Correlación**: Relaciones entre variables numéricas
- **Mapa de Calor**: Concentración laboral por país y habilidad
- **Panel de Subgráficos**: Relación edad vs. experiencia y distribución de calificaciones

---

## Variables Principales

| Variable | Descripción |
|----------|-------------|
| `freelancer_ID` | Identificador único del freelancer |
| `name` | Nombre del freelancer |
| `gender` | Género (Female, Male, Other) |
| `age` | Edad en años |
| `country` | País de residencia |
| `language` | Idioma principal |
| `primary_skill` | Habilidad/especialidad principal |
| `years_of_experience` | Años de experiencia profesional |
| `hourly_rate (USD)` | Tarifa horaria en dólares |
| `rating` | Calificación promedio (0-5) |
| `is_active` | Estado activo del perfil (yes/no) |
| `client_satisfaction` | Satisfacción del cliente (%) |

---

## Requisitos y Dependencias

### Python
- Python 3.7+

### Librerías Necesarias
```
numpy>=1.19.0
pandas>=1.1.0
matplotlib>=3.3.0
```

### Instalación
```bash
pip install numpy pandas matplotlib
```

---

## Cómo Usar

### Opción 1: Ejecutar los Notebooks en orden

1. **Preparar los datos**
   ```
   notebooks/02_preparation.ipynb
   ```
   - Lee los datos crudos
   - Aplica transformaciones de limpieza
   - Guarda el dataset procesado

2. **Explorar los datos**
   ```
   notebooks/01_eda.ipynb
   ```
   - Analiza la estructura del dataset
   - Examina valores faltantes
   - Explora variables categóricas

3. **Visualizar resultados**
   ```
   notebooks/03_visualization.ipynb
   ```
   - Genera gráficos estadísticos
   - Analiza correlaciones
   - Crea visualizaciones avanzadas

### Opción 2: Usar las funciones del módulo `src`

```python
import pandas as pd
from src import preparation, plots

# Cargar y preparar datos
df = pd.read_csv('data/raw/global_freelancers_raw.csv')
df_limpio = preparation.estandarizar_genero(df)
df_limpio = preparation.limpiar_tarifa_hora(df_limpio)
df_limpio = preparation.null_a_medianas(df_limpio)

# Generar gráficos
plots.graficar_histograma_edades(df_limpio)
plots.graficar_torta_idioma(df_limpio)
plots.graficar_matriz_correlacion(df_limpio)
```