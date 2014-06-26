#!/usr/bin/env python
# -*- coding: UTF-8 -*-

import json
import re

f = file('items7.json', 'r')
persons = json.load(f)
for p in persons:
    print p['name'].encode('gbk', 'replace')
    #print p['description'].encode('gbk', 'replace')
print len(persons)
