import pandas as pd
from pathlib import Path

def load_data(file_path: str | Path) -> pd.DataFrame:
    """Carrega o dataset lidando com separadores decimais em Português/Inglês."""
    path = Path(file_path)
    if path.suffix == '.csv':
        # Tenta ler com ponto; se ler tudo como object, recarrega usando vírgula
        df = pd.read_csv(path)
        numeric_cols = df.select_dtypes(include=['float64', 'int64']).columns
        if len(numeric_cols) <= 2:  # Se quase nenhuma coluna for numérica, tenta decimal=','
            df = pd.read_csv(path, decimal=',')
        return df
    elif path.suffix in ['.xls', '.xlsx']:
        return pd.read_excel(path)
    raise ValueError(f"Formato não suportado: {path.suffix}")

def select_numeric_features(df: pd.DataFrame) -> pd.DataFrame:
    """Filtra atributos do solo e garante colunas numéricas válidas."""
    # 1. Filtra outliers se a coluna existir (e não zerar o dataset)
    if 'outlier' in df.columns:
        df_filtered = df[df['outlier'] == 0]
        if not df_filtered.empty:
            df = df_filtered

    # 2. Colunas não-analíticas a descartar
    cols_to_drop = ['ID', 'id', 'X-coord', 'Y-coord', 'SMZ', 'outlier', 'zona', 'cluster', 'Soybean yield (kg/ha)']
    df_features = df.drop(columns=[col for col in cols_to_drop if col in df.columns])

    # 3. Converte colunas de texto com números para float (caso tenham sobrado)
    for col in df_features.columns:
        if df_features[col].dtype == 'object':
            df_features[col] = pd.to_numeric(
                df_features[col].astype(str).str.replace(',', '.'), 
                errors='coerce'
            )

    # 4. Mantém apenas colunas numéricas sem variação nula
    df_numeric = df_features.select_dtypes(include=['float64', 'int64']).dropna(axis=1, how='all')
    df_numeric = df_numeric.loc[:, df_numeric.std() > 0]

    print(f"[DIAGNÓSTICO] Colunas numéricas selecionadas para o PCA ({df_numeric.shape[1]}):")
    print(list(df_numeric.columns))

    return df_numeric