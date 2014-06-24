from scrapy.spider import Spider
from scrapy.selector import Selector

from dirbot.items import Article

import json
import re
import string

class YouyousuiyueSpider(Spider):
    name = "youyousuiyue"
    allowed_domains = ["youyousuiyue.sinaapp.com"]
    
    start_urls = [
        'http://youyousuiyue.sinaapp.com',
    ]
        
    def parse(self, response):
        """
        The lines below is a spider contract. For more info see:
        http://doc.scrapy.org/en/latest/topics/contracts.html

        @url http://youyousuiyue.sinaapp.com
        @scrapes name
        """
        sel = Selector(response)
        items = []

        print sel
        articles = sel.xpath('//div[@id="content"]/article')
        print 'len(articles)=', len(articles)
        
        for d in articles:
            item = Article()
            title = d.xpath('header/h1/a')
            item['title'] = title.xpath('text()').extract()
            item['url'] = title.xpath('@href').extract()
            item['content'] = d.xpath('div[@class="entry-content"]/div/text()').extract()
            items.append(item)
        return items
