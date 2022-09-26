from turtle import title
import requests
import time
import webbrowser
from bs4 import BeautifulSoup


url = requests.get('https://articulo.mercadolibre.com.mx/MLM-1360987319-playera-hades-caballeros-del-zodiaco-damacaballeronino-_JM')
soup = BeautifulSoup(url.content, "html.parser")
result = soup.find("span", {"class":"andes-money-amount__fraction"})

startPriceText = result.text
print(startPriceText)



