from scrapy.spider import Spider
from scrapy.selector import Selector

from dirbot.items import Article

import json
import re
import string
from scrapy.http import Request

class YouyousuiyueSpider(Spider):
    name = "youyousuiyue0"
    allowed_domains = ["youyousuiyue.sinaapp.com"]
    
    start_urls = [
        'http://youyousuiyue.sinaapp.com',
    ]
        
    def parse_item(self, response):
        """
        The lines below is a spider contract. For more info see:
        http://doc.scrapy.org/en/latest/topics/contracts.html

        @url http://youyousuiyue.sinaapp.com
        @scrapes name
        """
        sel = Selector(response)
        items = []

        articles = sel.xpath('//div[@id="content"]/article')
        
        for d in articles:
            item = Article()
            title = d.xpath('header/h1/a')
            item['title'] = title.xpath('text()').extract()
            print item['title'][0]
            item['url'] = title.xpath('@href').extract()
            item['content'] = d.xpath('div[@class="entry-content"]/div/text()').extract()
            items.append(item)
        return items

    def parse(self, response):
        """
        The lines below is a spider contract. For more info see:
        http://doc.scrapy.org/en/latest/topics/contracts.html

        @url http://youyousuiyue.sinaapp.com
        @scrapes name
        """
        
        print 'parsing ', response.url
        yield Request(response.url, callback=self.parse_item)

        sel = Selector(response)
        link = sel.xpath('//div[@class="nav-previous"]/a/@href').extract()[0]
        if link[-1] == '4':
            return
        else:
            print 'yielding ', link
            yield Request(link, callback=self.parse)
