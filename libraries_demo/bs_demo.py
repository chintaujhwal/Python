import requests
from bs4 import BeautifulSoup

link = requests.get("https://www.behance.net/")
bs = BeautifulSoup(link.text, "html.parser")

for t in bs.find_all("img"):
    if 'src' in t.attrs:
        print(t['src'])