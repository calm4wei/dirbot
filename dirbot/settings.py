# Scrapy settings for dirbot project

SPIDER_MODULES = ['dirbot.spiders']
NEWSPIDER_MODULE = 'dirbot.spiders'
DEFAULT_ITEM_CLASS = 'dirbot.items.Website'
LOG_ENABLED = False
#ITEM_PIPELINES = {'dirbot.pipelines.FilterWordsPipeline': 1}
