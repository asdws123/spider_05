# -*- coding: utf-8 -*-
import scrapy


class BaiduSpider(scrapy.Spider):
    #name:爬虫名
    #运行爬虫：scrapy crawl 爬虫名  
    name = 'baidu'
    #允许抓取的域名
    allowed_domains = ['www.baidu.com']
    #起始的url
    start_urls = ['http://www.baidu.com/']

    def parse(self, response):
        '''解析提取数据'''
        pass
