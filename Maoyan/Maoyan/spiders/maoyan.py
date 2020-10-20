# -*- coding: utf-8 -*-
import scrapy
from ..items import MaoyanItem

class MaoyanSpider(scrapy.Spider):
    name = 'maoyan'
    allowed_domains = ['maoyan.com']

    def start_requests(self):
        for i in range(10):
            page_url='https://maoyan.com/board/4?offset={}'.format(i*10)
            #将地址传给调度器入队
            yield scrapy.Request(url=page_url,callback=self.parse)

    def parse(self, response):
        dd_list = response.xpath('//dl[@class="board-wrapper"]/dd')
        for dd in dd_list:
            item = MaoyanItem()
            item['name'] = dd.xpath('.//p[@class="name"]/a/text()').get().strip()
            item['star'] = dd.xpath('.//p[@class="star"]/text()').get().strip()
            item['time'] = dd.xpath('.//p[@class="releasetime"]/text()').get().strip()

            yield item












