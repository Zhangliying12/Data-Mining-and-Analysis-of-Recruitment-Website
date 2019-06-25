# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class ArticleSpiderItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    position = scrapy.Field()
    salary = scrapy.Field()
    experience_and_degree = scrapy.Field()
    work_place = scrapy.Field()
    company_name = scrapy.Field()
    industry = scrapy.Field()
    bonus = scrapy.Field()
    url = scrapy.Field()