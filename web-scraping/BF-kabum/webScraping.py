import time
import json
import requests
import pandas as pd
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.firefox.options import Options

url = "https://www.kabum.com.br/"

option = Options()
option.headless = True                          # True = o navegador não abre, False = o navegador abre
driver = webdriver.Firefox(options=option)

driver.get(url)


time.sleep(10) # sleep de 10 segundos pra ter certeza qua a pagina carregou completamente

driver.quit()