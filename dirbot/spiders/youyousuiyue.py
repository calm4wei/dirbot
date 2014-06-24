from scrapy.spider import Spider
from scrapy.selector import Selector

from dirbot.items import Article

import json
import re
import string
from scrapy.http import Request

class YouyousuiyueSpider(Spider):
    name = "youyousuiyue"
    allowed_domains = ["youyousuiyue.sinaapp.com"]
    
    start_urls = [
        'http://youyousuiyue.sinaapp.com',
    ]
        
    def load_item(self, d):
        item = Article()
        title = d.xpath('header/h1/a')
        item['title'] = title.xpath('text()').extract()
        print item['title'][0]
        item['url'] = title.xpath('@href').extract()
        item['content'] = d.xpath('div[@class="entry-content"]/div/text()').extract()
        return item

    def parse(self, response):
        """
        The lines below is a spider contract. For more info see:
        http://doc.scrapy.org/en/latest/topics/contracts.html

        @url http://youyousuiyue.sinaapp.com
        @scrapes name
        """
        
        print 'parsing ', response.url
        sel = Selector(response)
        articles = sel.xpath('//div[@id="content"]/article')
        for d in articles:
            yield self.load_item(d)

        sel = Selector(response)
        link = sel.xpath('//div[@class="nav-previous"]/a/@href').extract()[0]
        if link[-1] == '4':
            return
        else:
            print 'yielding ', link
            yield Request(link, callback=self.parse)
