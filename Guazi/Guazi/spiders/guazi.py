# -*- coding: utf-8 -*-
import scrapy
from ..items import GuaziItem

class GuaziSpider(scrapy.Spider):
    name = 'guazi'
    allowed_domains = ['www.guazi.com']
    # start_urls = ['https://www.guazi.com/www/buy/o1c-1/#bread']

    def start_requests(self):
        for i in range(10):
            page_url='https://www.guazi.com/www/buy/o{}c-1/#bread'.format(i)
            #将地址传给调度器入队
            yield scrapy.Request(url=page_url,callback=self.parse)

    def parse(self, response):
        '''提取数据'''
        li_list=response.xpath('//ul[@class="carlist clearfix js-top"]/li')
        for li in li_list:
            #给items.py中的GuaziItem类做实例化
            item=GuaziItem()
            item['name']=li.xpath('./a/@title').get()
            item['price']=li.xpath('.//div[@class="t-price"]/p/text()').get()
            item['link']=li.xpath('./a/@href').get()
        
            #数据传输给管道pipelines.py
            yield item

