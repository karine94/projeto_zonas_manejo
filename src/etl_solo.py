import os
import numpy as np
import pandas as pd


def executar_etl():
    # Caminhos dos arquivos
    caminho_raw = "data/raw/data_smz_eca_curitibanos.csv"
    pasta_processed = "data/processed"
    caminho_processed = os.path.join(pasta_processed, "solo_tratado.csv")

    print("🔄 Iniciando pipeline de ETL dos dados de solo...")

    # 1. Verificar se o arquivo bruto existe na pasta data/raw/
    if not os.path.exists(caminho_raw):
        print(f"❌ Erro: Arquivo '{caminho_raw}' não encontrado!")
        print(
            "Certifique-se de salvar 'data_smz_eca_curitibanos.csv' na pasta 'data/raw/' e tente novamente."
        )
        return

    # 2. Carregar dados brutos
    df = pd.read_csv(caminho_raw)
    print(
        f"📥 Dados brutos carregados com sucesso: {df.shape[0]} linhas e {df.shape[1]} colunas."
    )

df.head()  # Exibe as primeiras linhas do DataFrame para inspeção
    # 3. Tratamento e Limpeza dos Dados
    # Remove linhas completamente duplicadas, se existirem
    df = df.drop_duplicates()

    # Preenche eventuais valores ausentes (NaN) com a mediana da coluna (apenas colunas numéricas)
    colunas_numericas = df.select_dtypes(include=[np.number]).columns
    df[colunas_numericas] = df[colunas_numericas].fillna(
        df[colunas_numericas].median()
    )

    # 4. Criar a pasta data/processed/ caso ainda não exista
    os.makedirs(pasta_processed, exist_ok=True)

    # 5. Salvar o arquivo tratado
    df.to_csv(caminho_processed, index=False)
    print(f"💾 Arquivo salvo com sucesso em: '{caminho_processed}'")
    print("✔ Pipeline de ETL concluída com sucesso!")


if __name__ == "__main__":
    executar_etl()