import requests
from bs4 import BeautifulSoup

req = requests.get("https://etea.edu.pk/result")
soup = BeautifulSoup(req.content, "html.parser")

res = soup.get(id="899")

print(soup.res)