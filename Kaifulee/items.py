# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class KaifuleeItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    title = scrapy.Field()
    classification = scrapy.Field()
    date = scrapy.Field()
    url = scrapy.Field()
    content = scrapy.Field()
    favorites = scrapy.Field()
    reads = scrapy.Field()
    comments = scrapy.Field()
    transfers = scrapy.Field()
    likes = scrapy.Field()
    pass
