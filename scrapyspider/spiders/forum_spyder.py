#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Fri Dec  8 12:37:57 2017

@author: apple
"""

from scrapy.spiders import Spider
from scrapyspider.items import ForumItem

class ForumSpider(Spider):
    name = 'forumspider'
    start_urls = ['https://www.manhattanprep.com/gmat/forums/gmat-prep-verbal-f31.html']
    
    def parse(self, response):
        
        item = ForumItem()
        forumlinks = response.xpath('//ul[@class="topiclist topics"]/li')
        for link in forumlinks:
            item['forumurl'] = link.xpath('.//dl/dt/div/a/@href').extract()[0]
            yield item
        
    