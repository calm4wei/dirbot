#!/usr/bin/env python
# -*- coding: UTF-8 -*-

import json
import re

f = file('iaf_map_clean1.json', 'r')
personMap = json.load(f)

names = personMap.keys()

enNames = {}
for n in names:
    v = personMap[n]
    mo = re.match(u'^.*（([^（）]*)）.*$', v['description'])
    if mo:
        en = mo.group(1).strip()
        en = en.replace(u'\xa0', ' ')
    	enNames[en] = n
        print en, n.encode('gbk', 'ignore')

print len(enNames)

f = file('iaf_en_names.json', 'w')
json.dump(enNames, f)
