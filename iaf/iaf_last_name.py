#!/usr/bin/env python
# -*- coding: UTF-8 -*-

import json
import re
import sys

f = file('iaf_names.txt', 'r')
persons = f.readlines()
f.close()

lnMap = {}
for p in persons:
    n = p.strip().decode('utf-8')
    mo = re.match(u'^(.*)·(.+)$', n)
    
    if mo:
        ln = mo.group(2)
        if lnMap.has_key(ln):
            lnMap[ln].append(n)
        else:
            lnMap[ln] = [n]

fout = file('last_name_count.txt', 'w')
for ln in lnMap.keys():
	s = '%s\t%d' % (len(lnMap[ln]))
	print s.encode('gbk')
	su = s.encode('utf-8')
	fout.write(su + '\n')

json.dump(lnMap, file('iaf_last_names.json', 'w'))
print len(lnMap)
#p1 = {}
#for k in lnMap.keys():
#    if len(lnMap[k]) == 1:
#        p1[k] = lnMap[k][0]

#persons = json.dump(p1, file('iaf_unique_names.json', 'w'))
