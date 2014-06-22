#!/usr/bin/env python
# -*- coding: UTF-8 -*-

import json
import re

f = file('items5.json', 'r')
s = f.read()
persons = json.loads(s)
c = 0
for p in persons:
    if len(p['name']) > 0:
        print p['name'][0]
        #print p['description'].encode('gbk', 'replace')
    else:
        print 'bad', p['url']
        print p['name']
        print p['description'].encode('gbk', 'replace')
        c = c+1
print len(persons)
print c