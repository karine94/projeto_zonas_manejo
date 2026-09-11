import numpy as np
import pandas as pd
from scipy.spatial.distance import mahalanobis

def filter_iqr(df: pd.DataFrame, factor: float = 1.5) -> pd.DataFrame:
    """Filtra outliers univariados com base na amplitude interquartil (IQR)."""
    q1 = df.quantile(0.25)
    q3 = df.quantile(0.75)
    iqr = q3 - q1
    mask = ~((df < (q1 - factor * iqr)) | (df > (q3 + factor * iqr))).any(axis=1)
    return df[mask]

def calculate_mahalanobis(df: pd.DataFrame) -> pd.Series:
    """Calcula a distância de Mahalanobis para diagnóstico multivariado."""
    cov_matrix = np.cov(df.values, rowvar=False)
    inv_cov_matrix = np.linalg.pinv(cov_matrix)
    mean_vector = df.mean().values

    distances = [
        mahalanobis(row.values, mean_vector, inv_cov_matrix) 
        for _, row in df.iterrows()
    ]
    return pd.Series(distances, index=df.index, name='mahalanobis')