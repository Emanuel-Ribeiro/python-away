from urllib.request import urlopen
from urllib.error import HTTPError
from urllib.error import URLError
from bs4 import BeautifulSoup

try:
    html = urlopen("https://www.kabum.com.br/")
except HTTPError as e:
    print(e)
except URLError:
    print("Servidor fora do ar ou dominio incorreto")
else:
    res = BeautifulSoup(html.read(),"html.parser")
    tags = res.findAll("h2", {"class": "H-titulo"})+res.findAll("div", {"class": "H-preco"})
    if res.title is None:
        print("Tag nao encontrada")
    else:
        print(res.title)
    for tag in tags:
      print(tag.getText())