# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class GuaziItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    #汽车名，价格，链接
    name=scrapy.Field()
    price=scrapy.Field()
    link=scrapy.Field()

    #相当与{'name':   ,'price':    ,'link':    }