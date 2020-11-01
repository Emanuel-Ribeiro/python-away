import time
import json
import requests
import pandas as pd
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.firefox.options import Options

url = "https://www.kabum.com.br/"

procura_termo = str(input("\nInsira o nome do produto desejado: "))
procura_termos = procura_termo.split(" ")

option = Options()
option.headless = False                          # True = o navegador não abre, False = o navegador abre
driver = webdriver.Firefox(options=option)

driver.get(url)

time.sleep(1)                                  # sleep de 10 segundos pra ter certeza qua a pagina carregou completamente

driver.find_element_by_xpath("//div[@id='BlocoBannerTopo']//a").click()

time.sleep(2)

elemento = driver.find_element_by_xpath("//div[@class='bloco-bg']//input[@id='input-busca']")
elemento.send_keys(procura_termo)
elemento.send_keys(Keys.ENTER)

teste = elemento.find_element_by_xpath("//div[@class='produto-info']")

html_content = teste.get_attribute('outerHTML')
print(html_content)

time.sleep(15)

driver.quit()