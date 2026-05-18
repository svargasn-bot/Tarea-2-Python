import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

df = pd.read_csv('../data/processed/global_freelancers_processed.csv')
imagenes_path = '../outputs/figures/'

# Distribucion Edades Freelancers
def graficar_histograma_edades(df):
    plt.figure(figsize=(8, 8))

    df['age'].plot(kind='hist', bins=20, color='skyblue', edgecolor='black')
    plt.title('Distribución de Edades de Freelancers', fontsize=14, fontweight='bold')
    plt.xlabel('Edad')
    plt.ylabel('Frecuencia')
    
    plt.savefig(imagenes_path + 'histograma_distribucion_edades.png')
    plt.show()

# Distribucion de idiomas
def graficar_torta_idioma(df, columna='language', titulo='Distribución de Idiomas'):
    counts = df[columna].value_counts()
    
    top_10 = counts.head(10)
    otros_valor = counts.iloc[10:].sum()
    otros_series = pd.Series({'Otros': otros_valor})
    datos_finales = pd.concat([top_10, otros_series])

    plt.figure(figsize=(8, 8))
    
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
    plt.savefig(imagenes_path + 'torta_idiomas.png')
    plt.show()

# Matriz de correlacion
def graficar_matriz_correlacion(df, columnas_num=None):
    if columnas_num is None:
        columnas_num = ['age', 'years_of_experience', 'hourly_rate (USD)', 'rating', 'client_satisfaction']
    
    # Nos aseguramos de filtrar solo las columnas que de verdad existan en el DataFrame
    columnas_validas = [col for col in columnas_num if col in df.columns]
    corr = df[columnas_validas].corr()
    
    fig, ax = plt.subplots(figsize=(8, 6))
    im = ax.matshow(corr, cmap='coolwarm')
    
    ax.set_xticks(range(len(corr.columns)))
    ax.set_xticklabels(corr.columns, rotation=45, ha='left')
    ax.set_yticks(range(len(corr.columns)))
    ax.set_yticklabels(corr.columns)
    
    plt.colorbar(im, ax=ax)
    
    fig.suptitle('Matriz de Correlación', fontsize=14, fontweight='bold')
    plt.tight_layout()
    plt.savefig(imagenes_path + 'matriz_correlacion.png')
    plt.show()

# Mapa de Calor: Concentración Laboral por Región
def graficar_mapa_de_calor(df):
    
    tabla_contingencia = pd.crosstab(df['country'], df['primary_skill'])
    
    # datos necesarios para colocar datos dentro de la matriz
    paises_top = tabla_contingencia.index.tolist()
    habilidades = tabla_contingencia.columns.tolist()
    matriz_datos = tabla_contingencia.values

    fig, ax = plt.subplots(figsize=(10, 6))
    cax = ax.imshow(tabla_contingencia.values, cmap='YlOrRd', aspect='auto')
    fig.colorbar(cax, label='Conteo de Freelancers')

    # con este codigo se ve el conteo de freelancers
    for i in range(len(paises_top)):
        for j in range(len(habilidades)):
            valor = matriz_datos[i, j]
            
            color_texto = "white" if valor > matriz_datos.max() * 0.75 else "black"
            
            ax.text(j, i, int(valor),
                    ha="center", va="center", 
                    color=color_texto, fontweight='bold', fontsize=10)


    ax.set_xticks(np.arange(len(habilidades)))
    ax.set_yticks(np.arange(len(paises_top)))
    ax.set_xticklabels(habilidades, rotation=45, ha='right', fontsize=9)
    ax.set_yticklabels(paises_top, fontsize=9)
    ax.set_title('Mapa de Calor: Concentración Laboral por Región', fontsize=13, fontweight='bold')

    plt.tight_layout()
    plt.savefig(imagenes_path + 'mapa_calor_paises.png')
    plt.show()

# Relación: Edad vs Años de Experiencia
def graficar_edad_experiencia(df, ax=None):
    # En caso de no ser un subgrafico, se toma el ax como nulo
    subgrafico = ax is None
    
    if subgrafico:
        fig, ax = plt.subplots(figsize=(8, 6))
    
    ax.scatter(df['age'], df['years_of_experience'], alpha=0.6, color='darkorange', s=30)
    coef = np.polyfit(df['age'], df['years_of_experience'], 1)
    polinomio = np.poly1d(coef)
    ax.plot(np.sort(df['age']), polinomio(np.sort(df['age'])), color='red', linewidth=2, label='Tendencia (r=0.62)')
    ax.set_title('Relación: Edad vs Años de Experiencia', fontsize=12, fontweight='bold')
    ax.set_xlabel('Edad (Años)', fontsize=10)
    ax.set_ylabel('Años de Experiencia', fontsize=10)
    ax.legend()
    
    if subgrafico:
        plt.savefig(imagenes_path + 'graficar_edad_experiencia.png')
        plt.close()
        plt.show()

# Frecuencia de Freelancers
def graficar_ratings(df, ax=None):
    subgrafico = ax is None
    
    if subgrafico:
        fig, ax = plt.subplots(figsize=(8, 6))
            
    ax.hist(df['rating'], bins=15, color='teal', alpha=0.7, edgecolor='white')
    ax.set_title('Distribución Global de Calificaciones (Ratings)', fontsize=12, fontweight='bold')
    ax.set_xlabel('Calificación (Rating)', fontsize=10)
    ax.set_ylabel('Frecuencia de Freelancers', fontsize=10)
    
    if subgrafico:
        plt.savefig(imagenes_path + 'graficar_ratings.png')
        plt.close()
        plt.show()

# Panel de subgraficos
def crear_panel_subgraficos(df):
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(15, 6))
    
    graficar_edad_experiencia(df, ax1)
    graficar_ratings(df, ax2)
    
    plt.tight_layout()
    plt.savefig(imagenes_path + 'edad_experiencia_y_ratings.png', dpi=300)
    plt.show()
