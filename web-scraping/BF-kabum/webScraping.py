import time
import json
import lxml
import requests
import pandas as pd
from lxml import html
from produto import Produto
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.firefox.options import Options

url = "https://www.kabum.com.br/"

procura_termo = str(input("\nInsira o nome do produto desejado: "))

maior_desconto = 0.0
menor_preco = 0.0
produto_mais_barato = Produto("", "", "", "")
melhor_custo_beneficio = Produto("", "", "", "")
procura_termos = procura_termo.split(" ")

option = Options()
option.headless = True                          # True = o navegador não abre, False = o navegador abre
driver = webdriver.Firefox(options=option)
option.add_argument('--ignore-certificate-errors')
option.add_argument('--incognito')
option.add_argument('--headless')

driver.get(url)

time.sleep(1)                                  # sleep de 10 segundos pra ter certeza qua a pagina carregou completamente

driver.find_element_by_xpath("//div[@id='BlocoBannerTopo']//a").click()

time.sleep(2)

elemento = driver.find_element_by_xpath("//div[@class='bloco-bg']//input[@id='input-busca']")
elemento.send_keys(procura_termo)
elemento.send_keys(Keys.ENTER)

produtos = []

time.sleep(1)

nome = elemento.find_element_by_xpath("//div[@class='produto-nome']").text
preco = elemento.find_element_by_xpath("//span[@class='produto-avista']").text
preco_anterior = elemento.find_element_by_xpath("//span[@class='produto-aprazo']//s").text

print(f"{nome}\nCusta: {preco}\nCustava: {preco_anterior}")

time.sleep(10)

driver.quit()