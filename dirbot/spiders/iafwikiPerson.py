from scrapy.spider import Spider
from scrapy.selector import Selector

from dirbot.items import Person

import json
import re
import string

class IafwikiPersonSpider(Spider):
    name = "iafwikiPerson"
    allowed_domains = ["zh.asoiaf.wikia.com"]
    url0 = "http://zh.asoiaf.wikia.com"
    
    f = file('items2.json', 'r')
    personLinks = json.load(f)
    start_urls = []
    for personLink in personLinks:
        start_urls.append(url0 + personLink['url'])
        
    #print start_urls

    def parse_item(self, response):
        """
        The lines below is a spider contract. For more info see:
        http://doc.scrapy.org/en/latest/topics/contracts.html

        @url http://zh.asoiaf.wikia.com/
        @scrapes name
        """
        sel = Selector(response)
        items = []

        descs = sel.xpath('//div[@id="mw-content-text"]/p[1]') # SelectorList
        
        for d in descs:
            item = Person()
            item['name'] = d.xpath('b[1]/text()').extract() # SelectorList[]
            t = string.join(d.xpath('node()').extract(), '').strip()
            t = re.sub(r'<[^<>]*>', '', t)
            t = re.sub(r'\[\d+\]', '', t)
            item['description'] = t
            item['url'] = response.url
            items.append(item)

        if len(items[0]['name']) <= 0:
            items = []
            descs = sel.xpath('//div[@id="mw-content-text"]/p[2]')
        
            for d in descs:
                item = Person()
                item['name'] = d.xpath('b[1]/text()').extract()
                t = string.join(d.xpath('node()').extract(), '').strip()
                t = re.sub(r'<[^<>]*>', '', t)
                t = re.sub(r'\[\d+\]', '', t)
                item['description'] = t
                item['url'] = response.url
                items.append(item)
        return items

    def parse(self, response):
        """
        The lines below is a spider contract. For more info see:
        http://doc.scrapy.org/en/latest/topics/contracts.html

        @url http://zh.asoiaf.wikia.com/
        @scrapes name
        """
        sel = Selector(response)
        items = []


        descs = sel.xpath('//div[@id="mw-content-text"]/p[1]') # SelectorList
        
        for d in descs:
            item = Person()
            item['name'] = d.xpath('b[1]/text()').extract() # SelectorList[]
            t = string.join(d.xpath('node()').extract(), '').strip()
            t = re.sub(r'<[^<>]*>', '', t)
            t = re.sub(r'\[\d+\]', '', t)
            item['description'] = t
            item['url'] = response.url
            items.append(item)

        if len(items[0]['name']) <= 0:
            items = []
            descs = sel.xpath('//div[@id="mw-content-text"]/p[2]')
        
            for d in descs:
                item = Person()
                item['name'] = d.xpath('b[1]/text()').extract()
                t = string.join(d.xpath('node()').extract(), '').strip()
                t = re.sub(r'<[^<>]*>', '', t)
                t = re.sub(r'\[\d+\]', '', t)
                item['description'] = t
                item['url'] = response.url
                items.append(item)
        return items
