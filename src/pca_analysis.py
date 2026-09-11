import pandas as pd
from sklearn.preprocessing import StandardScaler
from sklearn.decomposition import PCA
from factor_analyzer.factor_analyzer import calculate_bartlett_sphericity
import warnings
import numpy as np

def check_bartlett(df: pd.DataFrame) -> tuple[float | None, float | None]:
    """Retorna o Teste de Esfericidade de Bartlett tratando matrizes singulares."""
    with warnings.catch_warnings():
        warnings.simplefilter("ignore")
        try:
            chi2, p_value = calculate_bartlett_sphericity(df)
            if np.isnan(chi2):
                return None, None
            return chi2, p_value
        except Exception:
            return None, None

def run_pca(df: pd.DataFrame, n_components: int | None = None) -> tuple[PCA, pd.DataFrame]:
    """Padroniza os dados (Z-score) e executa o PCA."""
    scaler = StandardScaler()
    scaled_data = scaler.fit_transform(df)

    pca = PCA(n_components=n_components)
    pca_features = pca.fit_transform(scaled_data)

    cols = [f'PC{i+1}' for i in range(pca_features.shape[1])]
    df_pca = pd.DataFrame(pca_features, columns=cols, index=df.index)

    return pca, df_pca