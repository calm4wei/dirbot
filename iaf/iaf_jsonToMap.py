#!/usr/bin/env python
# -*- coding: UTF-8 -*-

import json
import re

f = file('iaf.json', 'r')
persons = json.load(f)
names = []
for p in persons:
    names.append(p['name'])
    print p['name'].encode('gbk', 'replace')
    #print p['description'].encode('gbk', 'replace')
print len(persons)

personMap = {}
for p in persons:
    personMap[p['name']] = {'url':p['url'], 'description':p['description']}

print len(personMap)
fout = file('iaf_map.json', 'w')
persons = json.dump(personMap, fout)
