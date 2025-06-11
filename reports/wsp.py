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

    start_urls = ["https://www.igrupos.com//whatsapp"]
    
    def parse(self, response):
        
        sel = Selector(response)
        preguntas = sel.xpath('//div[@class="media-body]')
        
        for pregunta in preguntas:
            item = ItemLoader(Pregunta(), pregunta)
            item.add_xpath('pregunta', './/a/h4/text()')
            item.add_xpath('descripcion', './/a/text()')
            yield item.load_item()
       
# COMANDO PARA EJECUTAR EL SPIDER EN CONSOLA
# scrapy runspider wsp.py -O result.json

