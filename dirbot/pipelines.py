#!/usr/bin/env python
# -*- coding: UTF-8 -*-

from scrapy.exceptions import DropItem
import re

class FilterWordsPipeline(object):
    """A pipeline for filtering out items which contain certain words in their
    description"""

    # put all words in lowercase
    
    words_to_filter = ['politics', 'religion']

    def process_item(self, item, spider):
        if re.match(r'^.*((\))|(\()|(船只)|(沙箱)|(规范)|(信条)|(维基)|(名片)|(版权)|(军备)|(药品)|(百科)|(严肃)|(方针)|(管理)|(申请)|(指南)|(/)|(\.\.\.)|(的)|(第[一二三四五六七八九十])).*$', item['name']):
            raise DropItem("Contains forbidden word: %s" % word)
        else:
            return item
