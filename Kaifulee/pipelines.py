# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html

import json
import codecs
import os
class KaifuleePipeline(object):
    def __init__(self):
        print("!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!init!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
        self.file = codecs.open("/tmp/KaifuleeBlog.json", "w", encoding='utf-8')

############# MAYBE ITEMLOADER
    def process_item(self, item, spider):
        line = json.dumps(dict(item), ensure_ascii=False) + "\n"
        print("!!!!!!!!!!!!!!there, writed!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
        self.file.write(line)
        return item

    def close_spider(self, spider):
        print('!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!close!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!')
        self.file.close()
