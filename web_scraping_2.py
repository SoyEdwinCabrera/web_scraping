from selenium import webdriver
from bs4 import BeautifulSoup

driver = webdriver.Chrome()
url = "https://www.cotodigital3.com.ar/sitios/cdigi/browse/catalogo-bebidas-bebidas-sin-alcohol-jugos/_/N-11la5tu"
driver.get(url)

html = driver.page_source
soup = BeautifulSoup(html, 'html.parser')

productos = soup.find_all('div', class_="product_info_container")

for producto in productos:
    span_nombre = producto.find('span', class_="span_productName")
    div_nombre = span_nombre.find('div')
    print(div_nombre.text.strip())
