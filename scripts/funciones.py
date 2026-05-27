import pandas as pd

def resumen_estadistico(df):
    return df.describe()

def contar_cumplimiento(df):
    return df["cumplimiento_norma"].value_counts()

