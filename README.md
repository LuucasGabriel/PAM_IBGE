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

## 🤖 Aprendizado Pessoal

Este projeto também marcou meu início nos estudos em **Python para análise de dados** sendo um divisor de águas para meu desenvolvimento.  

---

## 🙌 Agradecimentos

Se você chegou até aqui, minha gratidão!  
Estou totalmente aberto a **sugestões, melhorias e novas ideias** para evoluir ainda mais este projeto.  

---
