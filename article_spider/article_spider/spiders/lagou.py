# -*- coding: utf-8 -*-
import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
from article_spider.items import ArticleSpiderItem

class LagouSpider(CrawlSpider):
    name = 'lagou'
    allowed_domains = ['lagou.com']
    start_urls = ['https://lagou.com/']

    rules = (
        Rule(LinkExtractor(allow=r'Items/'), callback='parse_item', follow=True),
    )

    def parse_item(self, response):
        item = ArticleSpiderItem()
        item['title'] = response.xpath('//*[@id="s_position_list"]/ul//li/@data-positionname').extract()
        item['salary'] = response.xpath('//*[@id="s_position_list"]/ul//li/@data-salary').extract()
        item['experience_and_degree'] = response.xpath('//div[@class="p_bot"]/div[@class="li_b_l"]/text()').extract()
        return item
