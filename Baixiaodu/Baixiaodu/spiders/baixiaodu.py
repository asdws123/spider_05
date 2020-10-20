# -*- coding: utf-8 -*-
import scrapy


class BaixiaoduSpider(scrapy.Spider):
    name = 'baixiaodu'
    allowed_domains = ['www.baidu.com']
    start_urls = ['http://www.baidu.com/']

    def parse(self, response):
        #response:'http://www.baidu.com/'响应对象
        #response.xpath():[<selector xpath='' data=''>,<>]
        #extract():['a','b']
        #extract_first():'a'
        #get():等同于extract_first()--'a'
        # print(response.xpath('/html/head/title/text()').extract_first())
        print(response.xpath('/html/head/title/text()').get())

