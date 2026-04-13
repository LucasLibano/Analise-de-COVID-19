import requests
import pandas as pd

# URL da API
url = "https://disease.sh/v3/covid-19/countries"

# Requisição
response = requests.get(url)
data = response.json()

# Transformar em DataFrame
df = pd.DataFrame(data)

# Salvar como CSV
df.to_csv("dados_saude.csv", index=False)

# Salvar como Excel
df.to_excel("dados_saude.xlsx", index=False)

print("Arquivo salvo com sucesso!")