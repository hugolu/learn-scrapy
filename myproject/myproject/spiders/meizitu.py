# -*- coding: utf-8 -*-
import scrapy
from scrapy.selector import Selector

class MeizituSpider(scrapy.Spider):
    name = "meizitu"
    allowed_domains = ["www.meizitu.com"]
    start_urls = ['http://www.meizitu.com/']

    def parse(self, response):
        print('>>>>>> %s' % response.url)
        selector = Selector(response)

        links = selector.xpath('//div[@class="metaRight"]/h2/a/@href | //h3[@class="tit"]/a/@href').extract()
        for link in links:
            #print link
            request = scrapy.Request(link, callback = self.parse_item)
            yield request

        pages = selector.xpath('//div[@id="wp_page_numbers"]/ul/li/a/@href').extract()
        if len(pages) > 2:
            page = pages[-2]
            page = page.replace('/a/', '')
            request = scrapy.Request('http://www.meizitu.com/a/' + page, callback = self.parse)
            yield request
        pass


    def parse_item(self, response):
        print('  >>>> %s' % response.url)
        selector = scrapy.Selector(response)

        pics = selector.xpath('//div[@id="picture"]/p/img/@src').extract()
        for pic in pics:
            print('    >> %s' % pic)

        pass
