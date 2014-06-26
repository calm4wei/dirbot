#!/usr/bin/env python
# -*- coding: UTF-8 -*-

import json
import re

f = file('items1.json', 'r')
s = f.read()
persons = json.loads(s)
persons1 = []
c = 0
for p in persons:
    n = p['name'].encode('utf-8')
    if p['url'][:7] == '/wiki/%' and not re.match(r'^.*((\))|(\()|(船只)|(沙箱)|(规范)|(信条)|(维基)|(名片)|(版权)|(军备)|(药品)|(百科)|(严肃)|(方针)|(管理)|(申请)|(指南)|(/)|(\.\.\.)|(的)|(第[一二三四五六七八九十])).*$', n):
        if not re.match(r'^.*((号)|(集))$', n):
            print p['name'], p['url'][:18]
            persons1.append(p)
            c = c + 1
print len(persons)
print c
f = file('items2.json', 'w')
json.dump(persons1, f)
