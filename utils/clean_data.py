def clean_data(df):
    # Filtrar filas en función de las columnas: 'GENERO', 'TRAMO'
    # df = df[(df['GENERO'].str.contains("HOMBRE", regex=False, na=False, case=False)) & (df['TRAMO'].str.contains("A", regex=False, na=False, case=False))]
    # Seleccionar columnas: 'RUT', 'FECHA_NACIMIENTO' y 4 otras columnas
    df = df.loc[:, ['RUT', 'FECHA_NACIMIENTO', 'GENERO', 'TRAMO', 'NOMBRE_CENTRO', 'MOTIVO']]
    # Se ha realizado 1 agregación agrupados en columnas: 'NOMBRE_CENTRO', 'GENERO'
    df = df.groupby(['NOMBRE_CENTRO']).agg(RUT_count=('RUT', 'count')).reset_index()
    # Ordenar por columna: 'RUT_count' (descendente)
    df = df.sort_values(['RUT_count'], ascending=[False])
    return df