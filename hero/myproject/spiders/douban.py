# -*- coding: utf-8 -*-
import scrapy

import json

class DoubanSpider(scrapy.Spider):
    name = 'douban'
    allowed_domains = ['douban.com']
    # start_urls = ['https://www.douban.com/group/shanghaizufang/discussion?start=0']

    def start_requests(self): # 由此方法通过下面链接爬取页面
        
        # 定义爬取的链接
        urls = [
            'https://www.douban.com/group/shanghaizufang/discussion?start=0',
        ]
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse) #爬取到的页面如何处理？提交给parse方法处理

    def parse(self, response):
        results = []
        trs = response.css('table.olt tr')
        for tr in trs:
            title = tr.css('td.title a::attr(title)').extract_first()
            href = tr.css('td.title a::attr(href)').extract_first()
            upodatetime = tr.css('td.time::text').extract_first()
            # yield {'title': title, 'href': href, 'upodatetime': upodatetime}
            results.append({'title': title, 'href': href, 'upodatetime': upodatetime})

        with open('douban.json', 'w', encoding='utf-8') as f:
            json.dump(results, f, ensure_ascii=False)

        self.log('保存文件: 成功')

        
        
