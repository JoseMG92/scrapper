import requests
import time
import webbrowser
from bs4 import BeautifulSoup

#Url del producto a buscar
url = requests.get('https://articulo.mercadolibre.com.mx/MLM-1360987319-playera-hades-caballeros-del-zodiaco-damacaballeronino-_JM')

#Parsea el html del sitio web
soup = BeautifulSoup(url.content, "html.parser")

#Busca el elemento de interés
result = soup.find("span", {"class":"andes-money-amount__fraction"}) 

#Quita el nombre de la etiqueta y deja solo el precio en número entero
startPriceText = result.text 

#Parsea el precio de string a int
priceNumber = int(startPriceText)

#Compara el precio del producto con un precio deseado
finishPrice = 300
if priceNumber < finishPrice:
    print("Bajo de precio")
else:
    print("No ha bajado")


