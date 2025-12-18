# 📊 Análise da Produção Agrícola – CATI Regional de Tupã/SP

Este projeto tem como objetivo analisar a **produção agrícola** na região da **CATI Regional de Tupã/SP**, utilizando dados oficiais do **PAM/IBGE**.  
Foram considerados **14 municípios** e três culturas de grande relevância econômica: **cana-de-açúcar, mandioca e amendoim (em casca)**.  

A análise contempla desde o **tratamento e integração dos dados** até a **visualização espacial (mapas coropléticos)** e a **estimativa de valor econômico da produção**.  

---

## 📂 Estrutura do Projeto

- `data/` → Arquivos de dados utilizados (IBGE, malha municipal)  
- `notebooks/` → Jupyter Notebooks com a análise passo a passo  
- `scripts/` → Funções auxiliares em Python  
- `outputs/` → Mapas, gráficos e tabelas gerados  

---

## 🔎 Principais Etapas

1. **Filtragem de Municípios** → seleção dos 14 municípios de interesse.  
2. **Seleção de Culturas** → cana-de-açúcar, mandioca e amendoim (em casca).  
3. **Integração de Bases** → junção entre dados do PAM/IBGE e da malha municipal.  
4. **Cálculo Econômico** → estimativa da receita baseada em preços médios fixos.  
5. **Visualização Geoespacial** → criação de mapas coropléticos e gráfico de dispersão.  

---

## 🛠️ Tecnologias Utilizadas

- **Python 3.x**  
- **Pandas** → manipulação de dados  
- **GeoPandas** → análise geoespacial  
- **Matplotlib e Seaborn** → visualização de gráficos e mapas  
- **Jupyter Notebook** → documentação e execução da análise  

---

## 📊 Resultados

Evolução temporal: séries 2015 – 2023 por cultura, com gráfico de linha.

Produção: Culturas mais produzidas na Regional.

Comparações regionais: top 5 municípios que possuem mais produção de Cana De açúcar, Mandioca e Amendoim.

Produtividade e eficiência: scatter (Gráfico de dispersão) Área plantada × Rendimento médio com tamanho do ponto proporcional à produção.

Valor econômico: Quais culturas tiveram um gasto maior para produção.

Estimativa de Lucro: Qual foi a receita que esses produtos geraram para os produtores

Mapas coropléticos: concentração espacial da produção, Cana, Mandioca e Amendoim nos 14 Municípios. 

Esses resultados oferecem uma visão clara da **importância econômica do agronegócio na região** e podem apoiar **políticas públicas, planejamento logístico e investimentos**.  

---

---

## 🤖 Machine Learning – Previsão da Produção Agrícola

Como etapa de evolução do projeto, foi implementado um **modelo de Machine Learning supervisionado** com o objetivo de **prever a produção agrícola do ano seguinte**, utilizando os dados históricos da base da **Produção Agrícola Municipal (PAM/IBGE)**.

O modelo foi aplicado especificamente às três culturas analisadas neste estudo:
- Cana-de-açúcar  
- Mandioca  
- Amendoim (em casca)  

---

### 🧠 Metodologia do Modelo

- Utilização de dados históricos no período de **2016 a 2023**
- Construção de uma **série temporal** com variáveis defasadas:
  - `qtd_lag_1`: produção do ano anterior  
  - `qtd_lag_2`: produção de dois anos anteriores  
- Definição das **variáveis explicativas (features)** e do **alvo (quantidade produzida)**
- Separação temporal entre **treino e teste**, respeitando a ordem cronológica dos dados
- Treinamento do modelo utilizando a biblioteca **Scikit-learn**

---

### 📈 Avaliação do Modelo

O desempenho do modelo foi avaliado utilizando métricas de regressão:

- **MAE (Erro Absoluto Médio):** 24.485  
- **MSE (Erro Quadrático Médio):** 2.666.126.106  
- **RMSE (Raiz do Erro Quadrático Médio):** 51.634  
- **R² (Coeficiente de Determinação):** **0,95**

O valor elevado de **R²** indica que o modelo conseguiu explicar bem a variabilidade dos dados históricos, apresentando **bom desempenho preditivo**.

---

### ✅ Validação com Dados Reais de 2024

Após a disponibilização dos dados oficiais de **2024 pelo IBGE**, o modelo foi validado com informações reais.

- O modelo conseguiu **capturar corretamente a queda na produção agrícola** observada em 2024
- A diferença numérica entre previsão e valor real ficou dentro do esperado para um modelo preditivo
- Essa validação reforça a **capacidade de generalização do modelo**, mesmo sem acesso aos dados de 2024 durante o treinamento

---

## 🤖 Aprendizado Pessoal

Este projeto também marcou meu início nos estudos em **Python para análise de dados** sendo um divisor de águas para meu desenvolvimento.  

---

## 🙌 Agradecimentos

Se você chegou até aqui, minha gratidão!  
Estou totalmente aberto a **sugestões, melhorias e novas ideias** para evoluir ainda mais este projeto.  

---
- Visualizar Análise em Python: [PAM - Produção Agrícula Municipal](https://github.com/LuucasGabriel/PAM_IBGE/blob/main/visualizando.ipynb)

- Artigo: [PAM - Produção Agrícula Municipal](https://www.linkedin.com/pulse/an%C3%A1lise-da-produ%C3%A7%C3%A3o-agr%C3%ADcola-na-cati-regional-de-tup%C3%A3sp-lucas-gabriel-opmdf/?trackingId=muKxNq2dQiCG%2Bvg7Bse0lQ%3D%3D)

