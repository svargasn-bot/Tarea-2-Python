import numpy as np
import pandas as pd

def estandarizar_genero(df):
    df_limpio = df.copy()
    gender_map = {
        'f': 'Female', 'female': 'Female', 'fem': 'Female',
        'm': 'Male', 'male': 'Male', 'masc': 'Male'
    }

    df_limpio['gender'] = df['gender'].astype(str).str.lower().str.strip().map(gender_map).fillna('Other')

    return df_limpio

def estandarizar_is_active(df):
    df_limpio = df.copy()
    active_map = {
        '1': 'yes', 'true': 'yes', 'yes': 'yes', 'y': 'yes',
        '0': 'no', 'false': 'no', 'n': 'no', 'no': 'no'
    }

    df_limpio['is_active'] = df['is_active'].astype(str).str.lower().str.strip().map(active_map).fillna('no')

    return df_limpio

def limpiar_tarifa_hora(df):
    df_limpio = df.copy()
    
    df_limpio['hourly_rate (USD)'] = (df_limpio['hourly_rate (USD)']
                                     .astype(str)
                                     .str.replace(r'[\$,USD]', '', regex=True)
                                     .replace('nan', np.nan)
                                     .astype(float))
    
    return df_limpio

def limpiar_satisfacion(df):
    df_limpio = df.copy()
    df_limpio['client_satisfaction'] = (df_limpio['client_satisfaction']
                                .astype(str)
                                .str.replace('%', '')
                                .replace('nan', np.nan)
                                .astype(float))
    
    return df_limpio

def null_a_medianas(df, columnas_num=None):
    df_limpio = df.copy()
    if columnas_num is None:
        columnas_num = ['age', 'years_of_experience', 'hourly_rate (USD)', 'rating', 'client_satisfaction']
    
    for col in columnas_num:
        if col in df_limpio.columns: 
            df_limpio[col] = df_limpio[col].fillna(df_limpio[col].median())
            
    return df_limpio