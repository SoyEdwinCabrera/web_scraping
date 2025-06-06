# Web Scraping 101

## Descripción

Este proyecto contiene múltiples ejemplos y scripts para realizar web scraping utilizando diferentes herramientas y enfoques. Los ejemplos incluyen el uso de librerías como `Scrapy`, `BeautifulSoup`, `requests`, y `Selenium`, aplicados a sitios web como MercadoLibre, StackOverflow, Wikipedia, y otros. El objetivo es aprender y demostrar técnicas de extracción de datos de páginas web, incluyendo el manejo de contenido dinámico y estático.

## Puntos principales del proyecto

1. **Scrapy**:
   - Implementación de spiders para extraer datos estructurados de sitios web.
   - Ejemplos incluyen spiders para MercadoLibre, StackOverflow, y otros.

2. **BeautifulSoup**:
   - Uso de esta librería para analizar y extraer datos de HTML estático.
   - Ejemplos incluyen scripts para Wikipedia y MercadoLibre.

3. **Selenium**:
   - Uso de Selenium para manejar contenido dinámico que requiere renderización de JavaScript.
   - Ejemplo incluye un script para extraer datos de Coto Digital.

4. **requests**:
   - Realización de solicitudes HTTP para obtener contenido HTML.
   - Ejemplos incluyen scripts para Wikipedia y MercadoLibre.

5. **XPath y Selectores CSS**:
   - Uso de selectores para localizar y extraer datos específicos de las páginas web.

6. **Exportación de datos**:
   - Los datos extraídos se guardan en archivos JSON para facilitar su análisis y uso posterior.

## Librerías utilizadas y comandos de instalación

### 1. Scrapy
- Framework para web scraping que permite construir spiders robustos.
- **Instalación**:
  ```bash
  pip install scrapy
  ```

### 2. BeautifulSoup
- Librería para analizar HTML y XML.
- **Instalación**:
  ```bash
  pip install beautifulsoup4
  ```

### 3. Selenium
- Herramienta para automatizar navegadores web.
- **Instalación**:
  ```bash
  pip install selenium
  ```
- **Nota**: También es necesario instalar el controlador del navegador correspondiente, como [ChromeDriver](https://chromedriver.chromium.org/).

### 4. requests
- Librería para realizar solicitudes HTTP.
- **Instalación**:
  ```bash
  pip install requests
  ```

### 5. lxml
- Librería para analizar y manipular XML y HTML.
- **Instalación**:
  ```bash
  pip install lxml
  ```

## Cómo ejecutar los scripts

1. **Scrapy spiders**:
   - Ejecutar un spider desde la consola:
     ```bash
     scrapy runspider nombre_del_spider.py -O archivo_de_salida.json
     ```

2. **Scripts con BeautifulSoup o requests**:
   - Ejecutar el script directamente con Python:
     ```bash
     python nombre_del_script.py
     ```

3. **Scripts con Selenium**:
   - Asegúrate de tener el controlador del navegador instalado y ejecuta el script:
     ```bash
     python nombre_del_script.py
     ```

## Estructura del proyecto

- `mercadolibre.py`: Spider para extraer datos de MercadoLibre.
- `ign.py`: Spider para extraer datos de IGN.
- `stackoverflow.py`: Script con BeautifulSoup para StackOverflow.
- `stackoverflow_scrapy.py`: Spider de Scrapy para StackOverflow.
- `web_scraping.py`: Script con BeautifulSoup para MercadoLibre.
- `web_scraping_2.py`: Script con Selenium para Coto Digital.
- `wikipedia.py`: Script con requests y lxml para Wikipedia.
- `wsp.py`: Spider de Scrapy para WhatsApp Groups.

Este README proporciona una visión general del proyecto y las herramientas utilizadas. ¡Listo para comenzar con el web scraping!