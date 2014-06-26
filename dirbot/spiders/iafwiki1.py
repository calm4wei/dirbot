#!/usr/bin/env python
# -*- coding: UTF-8 -*-

from scrapy.spider import Spider
from scrapy.selector import Selector
from scrapy.http import Request

from dirbot.items import Person
import re
import string

class IafwikiSpider(Spider):
    name = "iafwiki1"
    allowed_domains = ["zh.asoiaf.wikia.com"]
    url0 = "http://zh.asoiaf.wikia.com"
    start_urls = [
        "http://zh.asoiaf.wikia.com",
    ]

    def parse_item(self, response):
        item = response.meta['item']
        
        sel = Selector(response)

        desc = sel.xpath('//div[@id="mw-content-text"]/p[1]')
        if len(desc) > 0:
            d = desc[0]
            item['name'] = d.xpath('b[1]/text()').extract()
            if item['name'] == []:
                d = sel.xpath('//div[@id="mw-content-text"]/p[2]')[0]
                item['name'] = d.xpath('b[1]/text()').extract()
            
            if len(item['name']) > 0:
                item['name'] = item['name'][0]
                t = string.join(d.xpath('node()').extract(), '').strip()
                t = re.sub(r'<[^<>]*>', '', t)
                t = re.sub(r'\[\d+\]', '', t)
                item['description'] = t
                return item
  
    def parse(self, response):
        """
        The lines below is a spider contract. For more info see:
        http://doc.scrapy.org/en/latest/topics/contracts.html

        @url http://zh.asoiaf.wikia.com/
        @scrapes name
        """
        depth = response.meta['depth']
        if not depth:
            depth = 0
        
        sel = Selector(response)
        persons = sel.xpath('//a')

        for p in persons:
            item = Person()
            t_url = p.xpath('@href').extract()
            if len(t_url) > 0:
                t_url = t_url[0]
                n = p.xpath('text()').extract()
                if len(n) > 0:
                    n = n[0]
                    if t_url[:7] == '/wiki/%' and not re.match(u'^.*((\))|(\()|(《)|(》)|(船只)|(沙箱)|(规范)|(信条)|(维基)|(名片)|(版权)|(军备)|(药品)|(百科)|(严肃)|(方针)|(管理)|(申请)|(指南)|(/)|(\.\.\.)|(的)|(第[一二三四五六七八九十])).*$', n):
                        if not re.match(u'^.*((号)|(集))$', n):
                            item = Person()
                            item['name'] = n
                            item['url'] = self.url0 + t_url
                            print '.', #'yielding and parsing ', item['url']
                            yield Request(item['url'], meta={'item':item}, callback=self.parse_item);
                
        if depth >= 1:
            return

        links = sel.xpath('//a/@href').extract()
        for link in links:
            if link[:6] == '/wiki/':
                print 'depth = %d yielding %s' % (depth, link)
                yield Request(self.url0 + link, meta={'depth': depth+1}, callback=self.parse)
