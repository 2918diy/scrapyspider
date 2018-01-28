# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class ScrapyspiderItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    pass

class ForumItem(scrapy.Item):
    
    #URL
    forumurl = scrapy.Field()
    
class ForumContentItem(scrapy.Item):
    
    #question
    forumquestion = scrapy.Field()
    
    #ron's answers
    ronanswers = scrapy.Field()