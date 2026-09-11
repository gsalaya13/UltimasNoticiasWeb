import requests
from bs4 import BeautifulSoup
import pandas as pd

url = "https://thehackernews.com/"
response = requests.get(url)
response.encoding = 'utf-8'

soup = BeautifulSoup(response.text, "html.parser")
Noticias = soup.find_all("a", class_="story-link")

datos = []
for Noticia in Noticias:
    titulo_noticia = Noticia.find("h2", class_="home-title")
    fecha_emision = Noticia.find("span", class_="h-datetime")
    #.text sirve para que entre la informacion como texto y no como etiqueta
    # Extraer los hashtag o etiquetas de clasificacion de la noticia
    hashtag = Noticia.find("span", class_="h-tags")

    datos.append({
        "Noticia": titulo_noticia.text.strip() if titulo_noticia else None,
        "Fecha_Publicacion": fecha_emision.text.strip() if fecha_emision else None,
        "Hashtags": hashtag.text.strip() if hashtag else None
    })

df = pd.DataFrame(datos)
df.to_csv("ultimas_noticias", index=False)
print("Scraping exitoso y archivo ultimas_noticias.csv creado.")
