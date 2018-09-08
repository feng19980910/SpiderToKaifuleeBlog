# -*- coding: utf-8 -*-
import scrapy
import re
import urllib
import json
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
        date = response.css(".time.SG_txtc::text").extract()[0]

        UnderLine = response.url.find("_")
        titleId = "t" + response.url[UnderLine : -5]
        title = response.css("#" + titleId + "::text").extract()[0]


        content = "".join(response.css("#sina_keyword_ad_area2 *::text").extract()).strip()
        if content == "":
            content = "".join(response.css("#sina_keyword_ad_area2 p *::text").extract())

        classification = 'None'
        getClass = response.css("td>.SG_txtb+a::text").extract()
        if getClass != []:
            classification = getClass[0]

        modole_request = 'http://comet.blog.sina.com.cn/api?maintype={maintype}&uid={uid}&aids={aids}&requestId={requestId}'
        originUrl = response.url
        originRequeBegin = originUrl.find('_') + 1
        originRequeEnd = -5
        originReque = originUrl[originRequeBegin:originRequeEnd]
        maintype = 'num'
        uid = originReque[:8]
        aids = originReque[-6:]
        requestId = 'artices_numer_132' #########
        requestAPI = modole_request.format(maintype=maintype, uid=uid, aids=aids, requestId=requestId)
        thisRequest = urllib.request.Request(requestAPI)
        originJson = urllib.request.urlopen(thisRequest)
        originJson = originJson.read().decode('utf-8')
        jsonBegin = originJson.find('{')
        jsonEnd = originUrl.rfind('}')
        print("*****************" )
        print(jsonEnd)
        jsonContent = originJson[jsonBegin : jsonEnd - 1]
        jsonDict = json.loads(jsonContent)
        
        favorites = jsonDict[aids]['f']
        reads = jsonDict[aids]['r']
        comments = jsonDict[aids]['c']
        transfers = jsonDict[aids]['z']
        likes = jsonDict[aids]['d']


        item = KaifuleeItem()
        item['title'] = title
        item["classification"] = classification
        item["date"] = date
        item["url"] = articalUrl
        item["content"] = content
        item['favorites'] = favorites
        item['reads'] = reads
        item['comments'] = comments
        item['transfers'] = transfers
        item['likes'] = likes
        yield item
