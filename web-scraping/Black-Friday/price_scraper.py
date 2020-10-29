import requests 
import json
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from produto import Produto
from utils import convert_price_toNumber
from web_driver_conf import get_web_driver_options
from web_driver_conf import get_chrome_web_driver
from web_driver_conf import set_ignore_certificate_error
from web_driver_conf import set_browser_as_incognito
from web_driver_conf import set_automation_as_head_less

URL = "https://www.kabum.com.br/"
NUMERO_DE_PAGINAS_BUSCADAS = 10
PERGUNTA_PRODUTO = "Qual produto você proucura?\n:"
proucura_termo = str(input(PERGUNTA_PRODUTO))

maior_desconto = 0.0
menor_preco = 0.0
produto_mais_barato = Produto("", "", "", "")
melhor_custo_beneficio = Produto("", "", "", "")
proucura_termos = proucura_termo.split(" ")

options = get_web_driver_options()
set_automation_as_head_less(options)
set_ignore_certificate_error(options)
set_browser_as_incognito(options)
driver = get_chrome_web_driver(options)

driver.get(URL)
element = driver.find_element_by_xpath('//*[@id="twotabsearchtextbox"]')
element.send_keys(proucura_termo)
element.send_keys(Keys.ENTER)

produtos = []

pagina = NUMERO_DE_PAGINAS_BUSCADAS

while True:
    if pagina != 0:
        try:
            driver.get(driver.current_url + "&pagina=" + str(pagina))
        except:
            break

    for i in driver.find_elements_by_xpath('//*[@id="search"]/div[1]/div[2]/div/span[4]/div[1]'):
        counter = 0
        for element in i.find_elements_by_xpath('//div/div/div[2]/div[2]/div/div[2]/div[1]/div/div[1]/div/div/a'):
            should_add = True
            nome = ""
            preco = ""
            preco_anterior = ""
            link = ""
            try:
                nome = i.find_elements_by_tag_name('h2')[counter].text
                preco = convert_price_toNumber(element.find_element_by_class_name('a-price').text)
                link = i.find_elements_by_xpath('//h2/a')[counter].get_attribute("href")
                try:
                    preco_anterior = convert_price_toNumber(element.find_element_by_class_name('a-text-price').text)
                except:
                    Exception()
                    preco_anterior = preco
            except:
                print("exception")
                should_add = False
            produto = Produto(nome, preco, preco_anterior, link)
            if should_add:
                produtos.append(produto)
            counter = counter + 1
    pagina = pagina - 1
    if pagina == 0:
        break
    print(pagina)

run = 0

for produto in produtos:
    not_right = False
    for word in proucura_termos:
        if word.lower() not in produto.name.lower():
            not_right = True
    if not not_right:
        if run == 0:
            menor_preco = produto.price
            produto_mais_barato = produto
            run = 1
        elif produto.price < menor_preco:
            menor_preco = produto.price
            produto_mais_barato = produto
        discount = produto.prev_price - produto.price
        if discount > maior_desconto:
            maior_desconto = discount
            melhor_custo_beneficio = produto

with open('produtos.json', 'w') as json_file:
    data = {}
    data["produtos"] = []
    for prod in produtos:
        data["produtos"].append(prod.serialize())
    json.dump(data, json_file, sort_keys=True, indent=4)

print(json.dumps(produto_mais_barato.serialize(), indent=4, sort_keys=True))
print(json.dumps(melhor_custo_beneficio.serialize(), indent=4, sort_keys=True))

options = get_web_driver_options()
set_ignore_certificate_error(options)
driver = get_chrome_web_driver(options)
driver.get(melhor_custo_beneficio.link)
driver.find_element_by_tag_name('body').send_keys(Keys.COMMAND + 't')