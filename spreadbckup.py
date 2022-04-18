import requests
import pandas as pd
from time import sleep
import telebot

#importa o bot do telegram
CHAVE_API = "5105014312:AAF5hja--6ux0Ago26LUzsIsq0KY7P8JMnQ"
bot = telebot.TeleBot(CHAVE_API)

#importa a base de dados com os simbolos das moedas
base = pd.read_csv('crypto.csv')
listaMoedas = base['Simbolo'].tolist()

#preço dólar em real
precoDolar = float(requests.get('https://economia.awesomeapi.com.br/last/USD-BRL').json()['USDBRL']['bid'])
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
    porcentoBinancexMB = ((precoBinance/dolarMB)-1)*100
    porcentoBinancexNovaDax = ((precoBinance/dolarNovaDax)-1)*100

    difMBxNovaDax = dolarMB-dolarNovaDax

    if (porcentoBinancexMB >=0.02):
      print(f'Compra {moeda} no MB por {dolarMB} vende na binance por {precoBinance}')
    elif (porcentoBinancexMB <=-0.02):
      print(f'Compra {moeda} na Binance por {precoBinance} vende no MV por {dolarMB}')
    elif  (porcentoBinancexNovaDax >=0.02):
      print(f'Compra {moeda} na NovaDax por {dolarNovaDax} vende na binance por {precoBinance}')

  elif (requisicaoStatusMB == 200) and (requisicaoStatusNovaDax==200):
    precoMB = float(requests.get(f'https://www.mercadobitcoin.net/api/{moeda}/ticker').json()['ticker']['last'])
    precoNovaDax = float(requests.get(f'https://api.novadax.com/v1/market/ticker?symbol={moeda}_BRL').json()['data']['bid'])
    dolarMB = precoMB/precoDolar
    dolarNovaDax = precoNovaDax/precoDolar
    print('NÃO TEM NA BINANCE')
    print('-'* 40)
    print(f'{moeda} no MB {dolarMB:.2f}')
    print(f'{moeda} na NovaDax {dolarNovaDax:.2f}')
    print('-'* 40)
  else:  
    print(f'Sem par compatível de {moeda}')
