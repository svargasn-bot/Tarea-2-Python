import matplotlib.pyplot as plt
import pandas as pd

def graficar_histograma_edades(df):
    plt.figure(figsize=(8, 8))

    df['age'].plot(kind='hist', bins=20, color='skyblue', edgecolor='black')
    plt.title('Distribución de Edades de Freelancers', fontsize=14, fontweight='bold')
    plt.xlabel('Edad')
    plt.ylabel('Frecuencia')
    
    plt.show()

def graficar_torta_idioma(df, columna='language', titulo='Distribución de Idiomas'):
    """
    Toma un DataFrame, agrupa los valores fuera del Top 10 en 'Otros'
    y genera un gráfico de torta estéticamente profesional.
    """
    # Contar frecuencias de la columna elegida
    counts = df[columna].value_counts()

    # separar el Top 10 y agrupar el resto en "Otros"
    top_10 = counts.head(10)
    otros_valor = counts.iloc[10:].sum()
    otros_series = pd.Series({'Otros': otros_valor})
    datos_finales = pd.concat([top_10, otros_series])

    plt.figure(figsize=(8, 8))

    # Definir colores dinámicamente según la cantidad de elementos
    colores = plt.cm.Paired(range(len(datos_finales)))

    datos_finales.plot(
        kind='pie', 
        labels=datos_finales.index, 
        autopct='%1.1f%%', 
        startangle=110, 
        colors=colores,
        pctdistance=0.85,  
        labeldistance=1.1  
    ) 
    plt.title(titulo, fontsize=16, fontweight='bold')
    plt.ylabel('') 
    plt.tight_layout()
    plt.show()

def graficar_matriz_correlacion(df, columnas_num=None):
    if columnas_num is None:
        columnas_num = ['age', 'years_of_experience', 'hourly_rate (USD)', 'rating', 'client_satisfaction']
    
    # Nos aseguramos de filtrar solo las columnas que de verdad existan en el DataFrame
    columnas_validas = [col for col in columnas_num if col in df.columns]
    corr = df[columnas_validas].corr()
    
    # Crear el gráfico
    plt.figure(figsize=(8, 6))
    plt.matshow(corr, cmap='coolwarm', fignum=1)
    
    plt.xticks(range(len(corr.columns)), corr.columns, rotation=45, ha='left')
    plt.yticks(range(len(corr.columns)), corr.columns)
    
    # Agregar la barra de color al lado
    plt.colorbar()
    
    plt.title('Matriz de Correlación', pad=20, fontsize=14, fontweight='bold')
    plt.show()