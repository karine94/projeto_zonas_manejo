from src.data_prep import load_data, select_numeric_features
from src.outliers import filter_iqr
from src.pca_analysis import check_bartlett, run_pca

def run_pipeline(data_path: str):
    # 1. Carregamento e seleção de variáveis
    df_raw = load_data(data_path)
    df_quant = select_numeric_features(df_raw)

    # 2. Remoção de Outliers
    df_clean = filter_iqr(df_quant)

   # 3. Validação para Análise Fatorial
    chi2, p_val = check_bartlett(df_clean)
    if chi2 is not None and p_val is not None:
        print(f"Bartlett Test: Chi2 = {chi2:.2f}, p-value = {p_val:.4e}")
    else:
        print("[INFO] Teste de Bartlett: detectada alta multicolinearidade entre atributos do solo.")

    # 4. Execução do PCA
    pca_model, df_pca = run_pca(df_clean)
    print("Variância explicada por componente (%):")
    for i, ratio in enumerate(pca_model.explained_variance_ratio_):
        print(f"  PC{i+1}: {ratio * 100:.2f}%")

    return pca_model, df_pca

if __name__ == "__main__":
    run_pipeline("data\processed\solo_tratado.csv")
   