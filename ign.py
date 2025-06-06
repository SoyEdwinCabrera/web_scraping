from scrapy.item import Item, Field
from scrapy.spiders import CrawlSpider, Rule
from scrapy.selector import Selector
# from scrapy.loader.processors import MapCompose
from scrapy.linkextractors import LinkExtractor
from scrapy.loader import ItemLoader


class Articulo(Item):
    titulo = Field()
    descripcion = Field()
    
class Review(Item):
    titulo = Field()
    calificacion = Field()
    
class Video(Item):
    titulo = Field()
    fecha_de_publicacion = Field()
    
class MercadoLibreSpider(CrawlSpider):    
    name = 'mercadolibre'
    
    custom_settings = {
        'USER_AGENT': "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Ubuntu Chromium/71.0.3578.80 Chrome/71.0.3578.80 Safari/537.36",
        'CLOSESPIDER_PAGECOUNT': 10,  # Número máximo de páginas en las cuales voy a descargar items. Scrapy se cierra cuando alcanza este número.
    }
    
    allowed_domains = ['latam.ign.com']
    start_urls = ['https://latam.ign.com/se/?model=&q=ps4']
    download_delay = 1
    
    rules = (
        Rule(
            LinkExtractor(
                allow=r'type='),
                follow=True),
        
        Rule(
        LinkExtractor(
                allow=r'/video/'),
                follow=True, callback='parse_review'),
                
        Rule(
        LinkExtractor(
                allow=r'/news/'),
                follow=True, callback='parse_review'),
    )
    
    def parse_video(self, response):
        item = ItemLoader(Video(), response)
        item.add_xpath('titulo', '//h1/text()')
        item.add_xpath('fecha_de_publicacion', '//span[@class="publish-date"]/text()')
        yield item.load_item()
        
    def parse_new(self, response):
        item = ItemLoader(Articulo(), response)
        item.add_xpath('titulo', '//h1/text()')
        item.add_xpath('contenido', '//div[@id="id_text"]//*/text()')
        yield item.load_item()