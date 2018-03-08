# -*- coding: utf-8 -*-
import scrapy

from bolha_spider.items import BolhaSpiderItem

class BolhaSpider(scrapy.Spider):
    name = 'bolha'
    allowed_domains = ['bolha.com']
    start_urls = [
        'http://www.bolha.com/nepremicnine/stanovanja/?location=Podravska%2FMaribor%2FCenter%2F&adTypeH=02_Oddam%2F&reType=1-sobno',
        'http://www.bolha.com/nepremicnine/stanovanja/?location=Podravska%2FMaribor%2FKoro%C5%A1ka+vrata%2F&adTypeH=02_Oddam%2F&reType=1-sobno',
        'http://www.bolha.com/nepremicnine/stanovanja/?location=Podravska%2FMaribor%2FCenter%2F&adTypeH=02_Oddam%2F&reType=1.5-sobno',
        'http://www.bolha.com/nepremicnine/stanovanja/?location=Podravska%2FMaribor%2FKoro%C5%A1ka+vrata%2F&adTypeH=02_Oddam%2F&reType=1.5-sobno',
    ]

    def parse(self, response):
        # //div[@class="ad featured"]
        for featuredAd in response.xpath('//div[@class="ad"]'):
            item = BolhaSpiderItem()
            item['title'] = featuredAd.xpath('div[@class="coloumn content"]//h3/a/text()').extract()
            item['description'] = featuredAd.xpath('div[@class="coloumn content"]//text()').extract()
            item['link'] = featuredAd.xpath('div[@class="coloumn content"]//h3/a/@href').extract()
            item['price'] = featuredAd.xpath('div[@class="coloumn prices"]//div[@class="price"]//span/text()').extract()
            yield item
