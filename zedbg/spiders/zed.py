import scrapy
from scrapy.loader import ItemLoader
from itemloaders.processors import TakeFirst
from zedbg.items import Project


class ZedSpider(scrapy.Spider):
    name = 'zed'
    allowed_domains = ['zedbg.com']
    start_urls = ['http://zedbg.com/eu-%d0%bf%d1%80%d0%be%d0%b5%d0%ba%d1%82%d0%b8-'
                  '%d0%b8-%d0%bf%d1%80%d0%be%d0%b3%d1%80%d0%b0%d0%bc%d0%b8/']

    def parse(self, response):
        projects = response.xpath("//div[@class='vc_column-inner ']")
        projects = [project for project in projects if project.xpath(".//p")]
        for project in projects:
            item = ItemLoader(Project())
            item.default_output_processor = TakeFirst()

            content = project.xpath(".//text()").getall()
            content = " ".join(content)

            item.add_value('content', content.strip())

            yield item.load_item()