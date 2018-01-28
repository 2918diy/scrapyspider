#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Fri Dec  8 15:51:45 2017

@author: apple
"""

from scrapy import Request
from scrapy.spiders import Spider
from bs4 import BeautifulSoup


class Forum_Content_Spider(Spider):
    
    name = 'forum_content_spider'
    
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2785.143 Safari/537.36',
    }
    
    start_urls = ['https://www.manhattanprep.com/gmat/forums/gmat-prep-verbal-f31.html']
    
    '''def start_requests(self):
        yield Request(headers=self.headers)
        print ("ok")'''
    
    
    
    def parse(self, response):
        #hxs = HtmlXPathSelector(response)
        #item = ForumItem()
        fourumlinks = response.xpath('//ul[@class="topiclist topics"]/li/dl/dt/div/a/@href').extract()
        for url in fourumlinks:
            yield Request(url, callback=self.parse_post,dont_filter=True, meta={'url_num':fourumlinks.index(url)})
            print(url)

    def parse_post(self, response):
        
        #抓取问题
        question = response.xpath('//div[@class="content"][1]').extract()
        question.extend(["<div><p>this is Ron's answers for "+response.url+"</p></div>"])
        next_url = response.xpath('//div[@class="pagination"]/span/a/@href').extract()
        #抓取第一页的答案
        for answers in response.xpath('//div[@id="page-body"]/div[starts-with(@class,"post bg")]'):
            if answers.xpath('./div/dl/dt/a/text()').extract()[0] == 'RonPurewal':
               question.extend(answers.xpath('./div/div/div').extract())
        #将question和第一页的答案写入文件
        file_path = "/Users/apple/Desktop/python_crawl/scrapyspider/"+str(response.meta['url_num'])+".html"
        with open(file_path,'w+') as f:
            for content in question:
                f.write(content)
            f.close()
        #获取下一页的链接list
        if len(next_url)!=0:
            for url in next_url[0:int(len(next_url)/2)]:
                yield Request(url, callback=self.parse_content_post,dont_filter=True,meta={'key':file_path})

        
    def parse_content_post(self, response):
        #获取答案文件路径
        file_path = response.meta['key']
        #抓取答案
        content = []
        for answers in response.xpath('//div[@id="page-body"]/div[starts-with(@class,"post bg")]'):

            if answers.xpath('./div/dl/dt/a/text()').extract()[0] == 'RonPurewal':
               content.extend(answers.xpath('./div/div/div').extract())
               print(content)
        #将答案写入文件
        with open(file_path,'a') as f:
            for cont in content:
                f.write(cont)
            f.close()
        #self.logger.info("+++++++++++++++++")
        #self.logger.info(content)