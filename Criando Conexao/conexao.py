


import requests
import pandas as pd

# URL da API SIDRA (Tabela 1612, nível mesorregião SP, último ano)
url = "https://apisidra.ibge.gov.br/values/t/5457/n6/3555000,3503356, 3505807, 3519006, 3519204, 3520806, 3527405, 3534609, 3536000, 3540853, 3541802, 3543808, 3544707, 3545100/v/8331, 216, 214, 112 , 215 /p/2015, 2016, 2017, 2018, 2019, 2020, 2021, 2022, 2023/C782/all/f/u"

response = requests.get(url)

if response.status_code == 200 and response.text.strip() != "":
    # Converte para JSON
    data_json = response.json()
    
    # Transforma em DataFrame
    df = pd.DataFrame(data_json[1:], columns=data_json[0])
    
    # Salva em CSV
    df.to_csv("pam_ibge.csv", index=False, encoding="utf-8-sig")
    
    print("Arquivo CSV salvo com sucesso!")
    print(df.head())
else:
    print("Erro na requisição:", response.status_code)
    print(response.text)



