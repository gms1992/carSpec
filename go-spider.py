from scrapy.crawler import CrawlerProcess
from scrapy.utils.project import get_project_settings

from carspec.carscrap.spiders.CarSpecSpider import CarSpecSpider


process = CrawlerProcess(get_project_settings())
process.crawl(CarSpecSpider)
process.start()