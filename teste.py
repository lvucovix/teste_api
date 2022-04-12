import requests
from time import sleep

c = 1
#solicita a cada 2 segundos
while True:
    # recebe o preço via API da binance
    binanceMoeda = "BTC"
    binanceBase = "BRL"
    binanceSimbolo = binanceMoeda+binanceBase
    binanceRequisicao = requests.get(f"https://api.binance.com/api/v3/ticker/price?symbol={binanceSimbolo}").json()
    binancePreco = binanceRequisicao["price"]

    # recebe o preço via API do MB
    MBrequisicao = requests.get("https://www.mercadobitcoin.net/api/BTC/ticker").json()
    MBpreco = MBrequisicao['ticker']
    ultimoPrecoMB = MBpreco['last']


    # transforma os preços de sting para número
    binancePrecoFloat = float(binancePreco)
    MBPrecoFloat = float(ultimoPrecoMB)
    # compara os preços
    dif = binancePrecoFloat - MBPrecoFloat
    porcento = 1-(binancePrecoFloat/MBPrecoFloat)
    print('-'* 40)
    print(c)
    print(f'Valor na Binance é {binancePrecoFloat:.2f}')
    print(f'Valor no MB é: {MBPrecoFloat:.2f}')
    print(f'Diferença de valor: {dif:.2f}')
    print(f'Diferença percentual: {porcento:2.2%}')
    print('-'* 40)
    sleep(2)
    c+=1