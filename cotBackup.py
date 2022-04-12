import requests
import pandas as pd
from time import sleep

#importa a base de dados com os simbolos das moedas
base = pd.read_csv('crypto.csv')
listaMoedas = base['Simbolo'].tolist()
#par dolar de cada moeda
binanceBase = "USDT"

for moeda in listaMoedas:
  binanceRequisicaoStatus = requests.get(f"https://api.binance.com/api/v3/ticker/price?symbol={moeda+binanceBase}").status_code
  if binanceRequisicaoStatus == 200:
    binanceRequisicao = requests.get(f"https://api.binance.com/api/v3/ticker/price?symbol={moeda+binanceBase}").json()
    binancePreco = binanceRequisicao["price"]
    print(f'Valor de {moeda} é {binancePreco}')
  else:
    print('Sem par compatível')
