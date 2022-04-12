import requests
import pandas as pd
from time import sleep


moedas = pd.read_csv('crypto.csv')
simbolos = moedas['Simbolo'].tolist()
print(simbolos)