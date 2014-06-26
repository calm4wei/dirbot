#!/usr/bin/env python
# -*- coding: UTF-8 -*-

import json
import re

f = file('iaf_map.json', 'r')
persons = json.load(f)
print len(persons)

persons1 = {}
for n in persons.keys():
    newn = n
	
    if len(n) > 20:
	    continue

    mo = re.match(u'^.*((章节)|(《)|(》)).*$', newn)
    if mo:
	    continue

    mo = re.match(u'^“(.*)”$', newn)
    if mo:
	    newn = mo.group(1)
	
    mo = re.match(u'^(.*)（.*$', newn)
    if mo:
	    newn = mo.group(1)
	
    mo = re.match(u'^（(.*)$', newn)
    if mo:
	    newn = mo.group(1)

    mo = re.match(u'^(.*)）$', newn)
    if mo:
	    newn = mo.group(1)

    mo = re.match(u'^）(.*)$', newn)
    if mo:
	    newn = mo.group(1)

    mo = re.match(u'^的(.*)$', newn)
    if mo:
	    newn = mo.group(1)

    persons1[newn] = persons.pop(n)

print len(persons1)
f = file('iaf_map_clean.json', 'w')
json.dump(persons1, f)
