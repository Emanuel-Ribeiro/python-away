from urllib.request import urlopen
from urllib.error import HTTPError
from urllib.error import URLError
from bs4 import dammit
from bs4 import BeautifulSoup

try:
    html = urlopen("https://www.kabum.com.br/")
except HTTPError as e:
    print(e)
except URLError:
    print("Server down or incorrect domain")
else:
    res = BeautifulSoup(html.read(),"html.parser")
    tags = res.findAll("h2", {"class": "H-titulo"})
    tags1 = res.findAll("div", {"class": "H-preco"})
    if res.title is None:
        print("Tag not found")
    else:
        print(res.title)
    for tag in tags:
      print(tag.getText())
    for tag in tags1:
      print(tag.getText())
