# -*- coding: utf-8 -*-
import scrapy


class DoubanSpider(scrapy.Spider):
    name = 'douban'
    allowed_domains = ['douban.com']
    start_urls = ['https://www.douban.com/group/shanghaizufang/']

    # start_urls = ['http://www.budejie.com/text/']

    def parse(self, response):
        trs = response.css('table.olt > tbody > tr')
        for tr in trs:
            title = tr.css('td.title > a::attr(title)').extract_first()
            href = tr.css('td.title > a::attr(href)').extract_first()
            yield {'title': title, 'href': href}
            
        # lies = response.css('div.j-r-list >ul >li')
        # for li in lies:
        #     username = li.css('a.u-user-name::text').extract()
        #     content = li.css('div.j-r-list-c-desc a::text').extract()
        #     yield {'username': username, 'content': content}
