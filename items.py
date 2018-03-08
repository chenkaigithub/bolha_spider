# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class BolhaSpiderItem(scrapy.Item):
    title = scrapy.Field()
    description = scrapy.Field()
    link = scrapy.Field()
    price = scrapy.Field()
    pass
