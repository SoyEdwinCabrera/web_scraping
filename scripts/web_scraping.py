import requests
from bs4 import BeautifulSoup

url = "https://listado.mercadolibre.com.co/ropa-accesorios/calzado/tenis/hombre/_Container_fs-moda-calzado-v2#applied_filter_id%3DFILTRABLE_GENDER%26applied_filter_name%3DGénero%26applied_filter_order%3D3%26applied_value_id%3D18549360%26applied_value_name%3DHombre%26applied_value_order%3D1%26applied_value_results%3D3613%26is_custom%3Dfalse"

response = requests.get(url)

if response.status_code == 200:
    soup = BeautifulSoup(response.text, 'html.parser')
    productos = soup.find_all('div', class_="andes-card ui-search-result ui-search-result--core andes-card--flat andes-card--padding-16 andes-card--animated")

    for producto in productos:
        titulo = producto.find('h2', class_="ui-search-item__title")
        marca = producto.find('span', class_="ui-search-item__brand-discoverability ui-search-item__group__element")
        if titulo:
            print(titulo.text.strip()) 
        if marca:
            print(marca.text.strip())


else:
    print("Error al cargar la web, código:", response.status_code)
