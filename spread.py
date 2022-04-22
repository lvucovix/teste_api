import requests
import pandas as pd
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

c = 1
while c <5:
  print(f'{c}ª verificação')
  #Binance X MB
  print('Verificando Binance x MB') 
  for moeda in listaMoedas:
    requisicaoStatusBinance = requests.get(f'https://api.binance.com/api/v3/ticker/price?symbol={moeda+binanceBase}').status_code
    requisicaoStatusMB = requests.get(f'https://www.mercadobitcoin.net/api/{moeda}/ticker').status_code

    if (requisicaoStatusBinance == 200) and (requisicaoStatusMB == 200):
      precoBinance = float(requests.get(f'https://api.binance.com/api/v3/ticker/price?symbol={moeda+binanceBase}').json()['price'])
      precoMB = (float(requests.get(f'https://www.mercadobitcoin.net/api/{moeda}/ticker').json()['ticker']['last']))/precoDolar
      porcentoBinancexMB = ((precoBinance/precoMB)-1)*100
      
      if (porcentoBinancexMB >=28):
        print(f'Compra {moeda} no MB por {precoMB} vende na Binance por {precoBinance}')
        bot.send_message(-763471222, f'Compra {moeda} no MB por {precoMB} vende na Binance por {precoBinance}')
      elif (porcentoBinancexMB <=-28):
        print(f'Compra {moeda} na Binance por {precoBinance} vende no MB por {precoMB}')
        bot.send_message(-763471222, f'Compra {moeda} na Binance por {precoBinance} vende no MB por {precoMB}')

  #MB X NOVADAX
  print('Verificando MB x NovaDax')
  for moeda in listaMoedas:
    requisicaoStatusMB = requests.get(f'https://www.mercadobitcoin.net/api/{moeda}/ticker').status_code
    requisicaoStatusNovaDax = requests.get(f'https://api.novadax.com/v1/market/ticker?symbol={moeda}_BRL').status_code

    if (requisicaoStatusMB == 200) and (requisicaoStatusNovaDax == 200):
      precoMB = (float(requests.get(f'https://www.mercadobitcoin.net/api/{moeda}/ticker').json()['ticker']['last']))/precoDolar
      precoNovaDax = float(requests.get(f'https://api.novadax.com/v1/market/ticker?symbol={moeda}_BRL').json()['data']['bid'])/precoDolar
      porcentoMBxNovaDax = ((precoMB/precoNovaDax)-1)*100

      
      if (porcentoMBxNovaDax >=28):
        print(f'Compra {moeda} na NovaDax por {precoNovaDax} vende no MB por {precoMB}')
      elif (porcentoMBxNovaDax <=-28):
        print(f'Compra {moeda} no MB por {precoMB} vende na NovaDax por {precoNovaDax}')

  #Binance X NovaDax
  print('Verificando Binance x NovaDax')
  for moeda in listaMoedas:
    requisicaoStatusBinance = requests.get(f'https://api.binance.com/api/v3/ticker/price?symbol={moeda+binanceBase}').status_code
    requisicaoStatusNovaDax = requests.get(f'https://api.novadax.com/v1/market/ticker?symbol={moeda}_BRL').status_code

    if (requisicaoStatusBinance == 200) and (requisicaoStatusNovaDax == 200):
      precoBinance = float(requests.get(f'https://api.binance.com/api/v3/ticker/price?symbol={moeda+binanceBase}').json()['price'])
      precoNovaDax = float(requests.get(f'https://api.novadax.com/v1/market/ticker?symbol={moeda}_BRL').json()['data']['bid'])/precoDolar
      porcentoBinancexMB = ((precoBinance/precoNovaDax)-1)*100

      
      if (porcentoBinancexMB >=28):
        print(f'Compra {moeda} no MB por {precoNovaDax} vende na Binance por {precoBinance}')
      elif (porcentoBinancexMB <=-28):
        print(f'Compra {moeda} na Binance por {precoBinance} vende no MB por {precoNovaDax}')
  c+=1
