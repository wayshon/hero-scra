# -*- coding: utf-8 -*-
import scrapy

import json

class Product(scrapy.Item):
    title = scrapy.Field()
    href = scrapy.Field()
    comment = scrapy.Field()
    username = scrapy.Field()
    userlink = scrapy.Field()
    upodatetime = scrapy.Field()
    last_updated = scrapy.Field(serializer=str)

class DoubanSpider(scrapy.Spider):
    name = 'douban'
    allowed_domains = ['douban.com']
    # start_urls = ['https://www.douban.com/group/shanghaizufang/discussion?start=0']

    # 另外一种初始链接写法
    def start_requests(self): # 由此方法通过下面链接爬取页面
        group = getattr(self, 'group', 'shanghaizufang')  # 获取tag值，也就是爬取时传过来的参数

        url = 'https://www.douban.com/group/%s/discussion?start=0' % group
        yield scrapy.Request(url=url, callback=self.parse) #爬取到的页面如何处理？提交给parse方法处理
            

    # 如果是简写初始url，此方法名必须为：parse
    def parse(self, response):
        # results = []
        trs = response.css('table.olt tr')
        for tr in trs:
            title = tr.css('td.title a::attr(title)').extract_first()
            href = tr.css('td.title a::attr(href)').extract_first()
            comment = tr.css('td[nowrap="nowrap"][class=""]::text').extract_first()
            username = tr.css('td[nowrap="nowrap"] a::text').extract_first()
            userlink = tr.css('td[nowrap="nowrap"] a::attr(href)').extract_first()
            upodatetime = tr.css('td.time::text').extract_first()
            
            commentNum = 0
            if (comment):
                commentNum = int(comment)
            
            product = Product(title=title,href=href,comment=commentNum,username=username,userlink=userlink,upodatetime=upodatetime)

            yield product

            # results.append(dict(product))
            # results.append({'title': title, 'href': href, 'username': username, 'userlink': userlink, 'comment': commentNum, 'upodatetime': upodatetime})

        # with open('douban.json', 'a', encoding='utf-8') as f:
        #     json.dump(results, f, ensure_ascii=False)

        # self.log('保存文件: 成功')

        next_page = response.css('div.paginator > span.next a::attr(href)').extract_first()
        if next_page is not None: 
            next_page = response.urljoin(next_page)
            yield scrapy.Request(next_page, callback=self.parse)

        
        
