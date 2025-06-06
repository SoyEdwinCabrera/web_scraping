from scrapy.item import Item, Field
from scrapy.spiders import CrawlSpider, Rule
from scrapy.selector import Selector
# from scrapy.loader.processors import MapCompose
from scrapy.linkextractors import LinkExtractor
from scrapy.loader import ItemLoader
from bs4 import BeautifulSoup
import logging

class Articulo(Item):
    titulo = Field()
    descripcion = Field()
    
class MercadoLibreSpider(CrawlSpider):    
    name = 'mercadolibre'
    
    custom_settings = {
        'USER_AGENT': "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Ubuntu Chromium/71.0.3578.80 Chrome/71.0.3578.80 Safari/537.36",
        'CLOSESPIDER_PAGECOUNT': 10,  # Número máximo de páginas en las cuales voy a descargar items. Scrapy se cierra cuando alcanza este número.
    }
    
    allowed_domains = ['articulo.mercadolibre.com.co', 'listado.mercadolibre.com.co']
    
    start_urls = ['https://listado.mercadolibre.com.co/']
    
    download_delay = 1 
    
    rules = (
        Rule(
            LinkExtractor(
                allow=r'/_Desde_\d+'
            ), follow=True),
        Rule(
            LinkExtractor(
                allow=r'/MPE'
            ), follow=True, callback='parse_items'),
    )
    
    
    def parse_items(self, response):
        logging.info(f"Procesando URL: {response.url}")
        
        item = ItemLoader(Articulo(), response)
        
        item.add_xpath('titulo', '//h1[@class="ui-pdp-title"]/text()`')
        item.add_xpath('descripcion', '//div[@class="ui-pdp-description"]/p/text()')
        
        yield item.load_item()