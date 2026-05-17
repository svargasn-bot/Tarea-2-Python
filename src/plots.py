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
    # 1. Contar frecuencias de la columna elegida
    counts = df[columna].value_counts()

    # 2. Separar el Top 10 y agrupar el resto en "Otros"
    top_10 = counts.head(10)
    otros_valor = counts.iloc[10:].sum()
    otros_series = pd.Series({'Otros': otros_valor})

    # 3. Unir ambos para tener el set de datos final
    datos_finales = pd.concat([top_10, otros_series])

    # 4. Crear el gráfico de torta
    plt.figure(figsize=(8, 8))

    # Definir colores dinámicamente según la cantidad de elementos
    colores = plt.cm.Paired(range(len(datos_finales)))

    # Graficar con tu configuración estética exacta
    datos_finales.plot(
        kind='pie', 
        labels=datos_finales.index, 
        autopct='%1.1f%%', 
        startangle=110, 
        colors=colores,
        pctdistance=0.85,  
        labeldistance=1.1  
    ) 

    # 5. Estética final
    plt.title(titulo, fontsize=16, fontweight='bold')
    
    # Quitamos la etiqueta por defecto de pandas en el eje Y para que se vea más limpio
    plt.ylabel('') 
    
    plt.tight_layout()
    plt.show()