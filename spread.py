import requests
import pandas as pd
from time import sleep

#importa a base de dados com os simbolos das moedas
base = pd.read_csv('crypto.csv')
listaMoedas = base['Simbolo'].tolist()

#preço dólar em real
precoDolar = float(requests.get('https://economia.awesomeapi.com.br/last/USD-BRL').json()['USDBRL']['high'])
print(f'O preço do dólar é: {precoDolar}')

#par dolar de cada moeda BINANCE
binanceBase = 'USDT'

for moeda in listaMoedas:
  requisicaoStatusBinance = requests.get(f'https://api.binance.com/api/v3/ticker/price?symbol={moeda+binanceBase}').status_code
  requisicaoStatusMB = requests.get(f'https://www.mercadobitcoin.net/api/{moeda}/ticker').status_code
  requisicaoStatusNovaDax = requests.get(f'https://api.novadax.com/v1/market/ticker?symbol={moeda}_BRL').status_code
  if (requisicaoStatusBinance == 200) and (requisicaoStatusMB == 200) and (requisicaoStatusNovaDax==200):
    precoBinance = float(requests.get(f'https://api.binance.com/api/v3/ticker/price?symbol={moeda+binanceBase}').json()['price'])
    precoMB = float(requests.get(f'https://www.mercadobitcoin.net/api/{moeda}/ticker').json()['ticker']['last'])
    precoNovaDax = float(requests.get(f'https://api.novadax.com/v1/market/ticker?symbol={moeda}_BRL').json()['data']['bid'])
    dolarMB = precoMB/precoDolar
    dolarNovaDax = precoNovaDax/precoDolar
    # dif = precoBinance-dolarMB
    # porcento = 1-(precoBinance/dolarMB)
    print('-'* 40)
    print(f'Valor de {moeda} na binance R$ {precoBinance:.2f}')
    print(f'Valor de {moeda} no MB R$ {precoMB:.2f}')
    print(f'Valor de {moeda} na NovaDax R$ {precoNovaDax:.2f}')
    print(f'Valor de {moeda} no MB em dolar $ {dolarMB:.2f}')
    print(f'Valor de {moeda} na NovaDax em dolar $ {dolarNovaDax:.2f}')
    # print(f'Diferença de valor: $ {dif:.2f}')
    # print(f'Diferença percentual: {porcento:2.2%}')
    print('-'* 40)
  elif (requisicaoStatusMB == 200) and (requisicaoStatusNovaDax==200):
    precoMB = float(requests.get(f'https://www.mercadobitcoin.net/api/{moeda}/ticker').json()['ticker']['last'])
    precoNovaDax = float(requests.get(f'https://api.novadax.com/v1/market/ticker?symbol={moeda}_BRL').json()['data']['bid'])
    dolarMB = precoMB/precoDolar
    dolarNovaDax = precoNovaDax/precoDolar
    print('NÃO TEM NA BINANCE')
    print('-'* 40)
    print(f'Valor de {moeda} no MB R$ {precoMB:.2f}')
    print(f'Valor de {moeda} na NovaDax R$ {precoNovaDax:.2f}')
    print(f'Valor de {moeda} no MB em dolar $ {dolarMB:.2f}')
    print(f'Valor de {moeda} na NovaDax em dolar $ {dolarNovaDax:.2f}')
    print('-'* 40)
  else:  
    print(f'Sem par compatível de {moeda}')
