import requests
from lxml import html

encabezado ={
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3"
}

url = "https://www.wikipedia.org/"

respuesta = requests.get(url, headers=encabezado)

# Parsear el contenido HTML de la respuesta
parser = html.fromstring(respuesta.text)

# Extraer el título de la página de diferentes maneras
español = parser.get_element_by_id("js-link-box-es")
print(español.text_content())

español1 = parser.xpath("//a[@id='js-link-box-es']/strong/text()")
print(español1)

idiomas = parser.xpath("//div[contains(@class, 'central-featured-lang')]//strong/text()")

for idioma in idiomas:
    print(idioma)
