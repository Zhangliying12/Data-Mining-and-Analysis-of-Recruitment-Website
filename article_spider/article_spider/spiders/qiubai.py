# -*- coding: utf-8 -*-
import scrapy
from article_spider.items import ArticleSpiderItem

class QiubaiSpider(scrapy.Spider):
    name = 'qiubai'
    allowed_domains = ['lagou.com']
    start_urls = ['https://www.lagou.com/zhaopin/Java/?labelWords=label']



    def parse(self, response):
        item = ArticleSpiderItem()
        item['position'] = response.xpath('//*[@id="s_position_list"]/ul//li/@data-positionname').extract()
        item['salary'] = response.xpath('//*[@id="s_position_list"]/ul//li/@data-salary').extract()
        item['experience_and_degree'] = response.xpath('//div[@class="p_bot"]/div[@class="li_b_l"]/text()').extract()
        item['work_place'] = response.xpath('//span[@class="add"]/em/text()').extract()
        item['company_name'] = response.xpath('//div[@class="company_name"]/a/text()').extract()
        item['industry'] = response.xpath('//div[@class="industry"]/text()').extract()
        item['bonus'] = response.xpath('//div[@class="li_b_r"]/text()').extract()
        item['url'] = response.xpath('//div[@class="p_top"]/a/@href').extract()
        yield item
