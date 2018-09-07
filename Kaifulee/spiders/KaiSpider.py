# -*- coding: utf-8 -*-
import scrapy
import re
from scrapy.http import Request
from urllib import  parse
from Kaifulee.items import KaifuleeItem

class KaispiderSpider(scrapy.Spider):
    name = 'KaiSpider'
    allowed_domains = ['blog.sina.com.cn']
    start_urls = ['http://blog.sina.com.cn/s/articlelist_1197161814_0_1.html/']

    def parse(self, response):
        post_urls = response.css(".atc_title a::attr(href)").extract()
        for post_url in post_urls:
            yield Request(url=parse.urljoin(response.url, post_url), callback=self.parse_detail)

        next_url = response.css(".SG_pgnext a::attr(href)").extract()
        if next_url != []:
            yield Request(url=parse.urljoin(response.url, next_url[0]), callback=self.parse)
            print("next page : " + next_url[0])

    def parse_detail(self,response):
        articalUrl = response.url
        UnderLine = response.url.find("_")
        titleId = "t" + response.url[UnderLine : -5]
        title = response.css("#" + titleId + "::text").extract()[0]
        date = response.css(".time.SG_txtc::text").extract()[0]
        content = "".join(response.css("#sina_keyword_ad_area2 *::text").extract()).strip()
        if content == "":
            content = "".join(response.css("#sina_keyword_ad_area2 p *::text").extract())
        getClass = response.css("td>.SG_txtb+a::text").extract()
        if getClass == []:
            classification = "None"
        else:
            classification = getClass[0]

        item = KaifuleeItem()
        item['title'] = title
        item["classification"] = classification
        item["date"] = date
        item["url"] = articalUrl
        item["content"] = content
        return item