import time
import json
import lxml
import requests
import pandas as pd
import urllib.request as request
from lxml import html
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.firefox.options import Options

procura_termo = str(input("\nInsira o nome do produto desejado: "))

url = (f'https://b2lq2jmc06.execute-api.us-east-1.amazonaws.com/PROD/ofertas?campanha=blackfriday&app=1&limite=200&pagina=1&string={procura_termo}')

with request.urlopen(url) as response:
  
  if (response.getcode() == 200):
    source = response.read()
    dados = json.loads(source)
    print("Sucesso ao obter os dados da API")

    #dict_keys(['quant_ofertas', 'categorias', 'logar', 'produtos', 'oferta', 'ordem', 'encerradas', 'filtro', 'quant_paginas'])
  
  else:
    print("Ocorreu um erro na tentativa de obter os dados da API")

produtos = [produto for produto in dados['produtos']]

with open('produtos_kbm.json', 'w') as f:
  json.dump(produtos, f, indent = 4, sort_keys = True)

with open('produtos_kbm.json') as f:
  dados = json.load(f)

def lista_produtos(produto):
  return(produto['produto'], produto['vlr_normal'], produto['vlr_oferta'])

with open('produtos_kbm.json') as f:
  dados = json.load(f, object_hook= lista_produtos)
  
#https://www.pluralsight.com/guides/importing-data-from-json-resource-with-python