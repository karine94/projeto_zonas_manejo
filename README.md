# 🌾 Delimitação de Zonas de Manejo e Predição de Produtividade em Agricultura de Precisão

Este repositório contém uma pipeline completa de Ciência de Dados voltada para a Agricultura de Precisão, aplicando técnicas de análise multivariada e aprendizado de máquina para a delimitação de Zonas de Manejo (ZM) e modelagem da produtividade da cultura da soja.

---

## 📌 Resumo do Projeto

O objetivo do estudo é identificar a variabilidade espacial dos atributos físico-químicos do solo para delimitar regiões homogêneas em um talhão agrícola. Essa subdivisão possibilita a aplicação de insumos a taxa variável (como adubação e calagem) e permite quantificar quais características do solo exercem maior impacto no rendimento final da lavoura.

### Etapas do Desenvolvidas:
1. **ETL & Tratamento de Dados (CARD-01):** Ingestão, padronização de unidades e validação de 50 pontos de amostragem georreferenciados.
2. **Análise Multivariada & PCA (CARD-02):** Redução de dimensionalidade para eliminar a multicolinearidade entre atributos do solo.
3. **Clusterização Espacial com K-Means (CARD-03):** Subdivisão da área em Zonas de Manejo de alta e baixa produtividade.
4. **Modelagem Regressiva (CARD-04):** Avaliação do impacto do solo e das zonas na produtividade final (sacas/ha).

---

## 📊 Fonte dos Dados & Créditos

Os dados utilizados neste projeto são reais, georreferenciados e foram obtidos de repositório público de pesquisa científica:

* **Estudo de Origem:** *Site-Specific Management Zones Delineation Based on Apparent Soil Electrical Conductivity in Two Contrasting Fields of Southern Brazil*
* **Localização dos Dados:** Curitibanos - SC, Brasil
* **Atributos Analisados:** Coordenadas espaciais (UTM), Condutividade Elétrica Aparente (CEa), pH, Matéria Orgânica, Fósforo (P), Potássio (K), Argila, CTC e Produtividade de Soja (kg/ha convertida para sacas/ha).
* **Aviso de Atribuição:** Agradecimentos aos autores originais pela disponibilização da base de dados aberta para fins educacionais e de pesquisa.


## 🗺️ Mapa de Zonas de Manejo (QGIS)

![Mapa de Zonas de Manejo](docs/mapa_zonas_manejo.png)
