import requests
from bs4 import BeautifulSoup # pip install beautifulsoup4

# USER AGENT PARA PROTEGERNOS DE BANEOS

headers = {
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3"
}

# URL SEMILLA
url = "https://stackoverflow.com/questions"

# REQUERIMIENTO AL SERVIDOR
respuesta = requests.get(url, headers=headers)

# PARSEO DEL ARBOL CON BEAUTIFULSOUP
soup = BeautifulSoup(respuesta.text)

contenedor_de_preguntas = soup.find(id="questions")
lista_de_preguntas = contenedor_de_preguntas.find_all("div", class_="s-post-summary")

for pregunta in lista_de_preguntas:
    texto_pregunta = pregunta.find("h3").text
    descripcion_pregunta = pregunta.find("div", class_="s-post-summary--content-excerpt").text
    descripcion_pregunta = descripcion_pregunta.strip()  # Eliminar espacios en blanco al inicio y al final
    # descripcion_pregunta = descripcion_pregunta.replace("\n", " ").replace('r', '')  # Reemplazar saltos de línea por espacios
    print(texto_pregunta)
    print(descripcion_pregunta)