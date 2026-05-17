def estandarizar_genero(df):
    df_copia = df.copy()
    gender_map = {
        'f': 'Female', 'female': 'Female', 'fem': 'Female',
        'm': 'Male', 'male': 'Male', 'masc': 'Male'
    }

    df_copia['gender'] = df['gender'].astype(str).str.lower().str.strip().map(gender_map).fillna('Other')

    return df_copia

def estandarizar_is_active(df):
    df_copia = df.copy()
    active_map = {
        '1': 'yes', 'true': 'yes', 'yes': 'yes', 'y': 'yes',
        '0': 'no', 'false': 'no', 'n': 'no', 'no': 'no'
    }

    df_copia['is_active'] = df['is_active'].astype(str).str.lower().str.strip().map(active_map).fillna('no')

    return df_copia

def limpiar_tarifa_hora(df):
    df_copia = df.copy()
    
    df_copia['hourly_rate (USD)'] = (df_copia['hourly_rate (USD)']
                                     .astype(str)
                                     .str.replace(r'[\$,USD]', '', regex=True)
                                     .replace('nan', np.nan)
                                     .astype(float))
    
    return df_copia