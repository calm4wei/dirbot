#!/usr/bin/env python
# -*- coding: UTF-8 -*-

import json
import re
import sys

f = file('iaf_en_names.txt', 'r')
persons = f.readlines()
f.close()

lnMap = {}
for p in persons:
    n = p.strip().decode('utf-8')
    mo = re.match(u'^(.*)\s+([^\s]+)$', n)
    
    if mo:
        ln = mo.group(2)
        if lnMap.has_key(ln):
            lnMap[ln].append(n)
        else:
            lnMap[ln] = [n]

fout = file('en_last_name_count.txt', 'w')
for ln in lnMap.keys():
	s = '%s\t%d' %(ln, len(lnMap[ln]))
	print s
	fout.write(s + '\n')

json.dump(lnMap, file('iaf_en_last_names.json', 'w'))
print len(lnMap)
