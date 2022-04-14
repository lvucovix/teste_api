import requests
import pandas as pd
from time import sleep

#importa a base de dados com os simbolos das moedas
base = pd.read_csv('crypto.csv')
listaMoedas = base['Simbolo'].tolist()

#par dolar de cada moeda BINANCE
binanceBase = "USDT"

for moeda in listaMoedas:
  binanceRequisicaoStatus = requests.get(f"https://api.binance.com/api/v3/ticker/price?symbol={moeda+binanceBase}").status_code
  MBRequisicaoStatus = requests.get(f"https://www.mercadobitcoin.net/api/{moeda}/ticker").status_code
  print(moeda)
  print(binanceRequisicaoStatus)
  print(MBRequisicaoStatus)