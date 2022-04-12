import requests
import pandas as pd
from time import sleep

#importa a base de dados com os simbolos das moedas
base = pd.read_csv('crypto.csv')
listaMoedas = base['Simbolo'].tolist()

#preço dólar em real
atualurl = "https://economia.awesomeapi.com.br/last/USD-BRL"

requisicao = requests.get(atualurl).json()['USD']
precoDolar = float(requisicao['high'])

print(f"O preço do dólar é: {precoDolar}")


#par dolar de cada moeda
binanceBase = "USDT"

for moeda in listaMoedas:
  binanceRequisicaoStatus = requests.get(f"https://api.binance.com/api/v3/ticker/price?symbol={moeda+binanceBase}").status_code
  MBRequisicaoStatus = requests.get("https://www.mercadobitcoin.net/api/BTC/ticker").status_code
  if (binanceRequisicaoStatus == 200) and (MBRequisicaoStatus == 200):
    binanceRequisicao = requests.get(f"https://api.binance.com/api/v3/ticker/price?symbol={moeda+binanceBase}").json()
    binancePreco = float(binanceRequisicao["price"])
    MBrequisicao = requests.get(f"https://www.mercadobitcoin.net/api/{moeda}/ticker").json()
    MBTicker = MBrequisicao['ticker']
    PrecoMB = float(MBTicker['last'])
    MBDolar = PrecoMB/precoDolar
    dif = binancePreco-MBDolar
    porcento = 1-(binancePreco/MBDolar)
    print('-'* 40)
    print(f'Valor de {moeda} na binance R$ {binancePreco:.2f}')
    print(f'Valor de {moeda} no mb R$ {PrecoMB:.2f}')
    print(f'Valor de {moeda} no mb em dolar $ {MBDolar:.2f}')
    print(f'Diferença de valor: $ {dif:.2f}')
    print(f'Diferença percentual: {porcento:2.2%}')
    print('-'* 40)
  else:
    print(f'Sem par compatível de {moeda}')
