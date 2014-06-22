from scrapy.spider import Spider
from scrapy.selector import Selector

from dirbot.items import PersonLink


class IafwikiSpider(Spider):
    name = "iafwiki"
    allowed_domains = ["zh.asoiaf.wikia.com/"]
    start_urls = [
        "http://zh.asoiaf.wikia.com/",
    ]

    def parse(self, response):
        """
        The lines below is a spider contract. For more info see:
        http://doc.scrapy.org/en/latest/topics/contracts.html

        @url http://zh.asoiaf.wikia.com/
        @scrapes name
        """
        sel = Selector(response)
        persons = sel.xpath('//a[@class="subnav-3a"]')
        items = []

        for p in persons:
            item = PersonLink()
            item['name'] = p.xpath('text()').extract()[0]
            item['url'] = p.xpath('@href').extract()[0]
            items.append(item)

        return items
