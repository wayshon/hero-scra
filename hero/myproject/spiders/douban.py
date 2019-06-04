# -*- coding: utf-8 -*-
import scrapy

# class CellItem(scrapy.Item):
#     title = scrapy.Field()
#     href = scrapy.Field()
#     author = scrapy.Field()
#     upodatetime = scrapy.Field()

class DoubanSpider(scrapy.Spider):
    name = 'douban'
    allowed_domains = ['douban.com']
    start_urls = ['https://www.douban.com/group/shanghaizufang/discussion?start=0']

    def parse(self, response):
        trs = response.css('table.olt tr')
        for tr in trs:
            title = tr.css('td.title a::attr(title)').extract_first()
            href = tr.css('td.title a::attr(href)').extract_first()
            upodatetime = tr.css('td.time::text').extract_first()
            yield {'title': title, 'href': href, 'upodatetime': upodatetime}

        # a = response.css('a.j.a_show_login.bn-join-group > span::text').extract_first()

        # a = response.css('table.olt td.title a::attr(title)').extract_first()
        # yield {'title': a, 'href': a}
        
