from scrapy.item import Item, Field
from scrapy.spiders import Spider
from scrapy.selector import Selector
# from scrapy.loader.processors import MapCompose
from scrapy.loader import ItemLoader
# from bs4 import BeautifulSoup

class Pregunta(Item):
    pregunta = Field()
    descripcion = Field()
    
class StackOverflowSpider(Spider):
    name = "miPrimerSpider"
    
    custom_settings = {
        "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3"
    }

    start_urls = ["https://stackoverflow.com/questions"]
    
    def parse(self, response):
        
        sel = Selector(response)
        preguntas = sel.xpath('//div[@id="questions"]//div[@class="s-post-summary"]')
        print(f"Preguntas encontradas: {len(preguntas)}") 
        for pregunta in preguntas:
            item = ItemLoader(Pregunta(), pregunta)
            item.add_xpath('pregunta', './/h3/a/text()')
            item.add_xpath('descripcion', './/div[@class="s-post-summary--content-excerpt"]/text()')
            yield item.load_item()
       
# COMANDO PARA EJECUTAR EL SPIDER EN CONSOLA
# scrapy runspider stackoverflow_scrapy.py -O result.json

# ESTE SCRIPT PUEDE NO FUCIONAR EN LA VERSIÓN ACTUAL DE SCRAPY 
# YA QUE ACTUALMENTE EL CONTENIDO DE LA PÁGINA ES DINAMICO Y SE CARGA CON JAVASCRIPT, 
# POR LO QUE ES NECESARIO USAR UN NAVEGADOR HEADLESS O UN SERVICIO DE RENDERIZACIÓN 
# COMO SCRAPY-SPLASH O SELENIUM PARA OBTENER LOS DATOS CORRECTAMENTE.