def clean_data_percapita(df):
    # Filtrar filas en función de las columnas: 'GENERO', 'TRAMO'
    # df = df[(df['GENERO'].str.contains("HOMBRE", regex=False, na=False, case=False)) & (df['TRAMO'].str.contains("A", regex=False, na=False, case=False))]
    # Seleccionar columnas: 'RUT', 'FECHA_NACIMIENTO' y 4 otras columnas
    df = df.loc[:, ['FECHA_CORTE', 'NOMBRE_CENTRO', 'EDAD', 'GENERO', 'MOTIVO', 'CODIGO_CMV', 'Recuento']]
    # Se ha realizado 1 agregación agrupados en columnas: 'NOMBRE_CENTRO', 'GENERO'
    df = df.groupby(['NOMBRE_CENTRO']).agg(CENTRO_count=('NOMBRE_CENTRO', 'count')).reset_index()
    # Ordenar por columna: 'RUT_count' (descendente)
    df = df.sort_values(['CENTRO_count'], ascending=[False])
    return df