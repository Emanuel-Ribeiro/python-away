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
    if res.title is None:
        print("Tag not found")
    else:
        print(res.title)