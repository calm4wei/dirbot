#!/usr/bin/env python
# -*- coding: UTF-8 -*-

import json
import re
import sys

f = file('iaf_names.txt', 'r')
persons = f.readlines()
f.close()

fnMap = {}
for p in persons:
    n = p.strip().decode('utf-8')
    mo = re.match(u'^([^·]*)·.*$', n)
    
    if mo:
        fn = mo.group(1)
        if fnMap.has_key(fn):
            fnMap[fn].append(n)
        else:
            fnMap[fn] = [n]

fout = file('first_name_count.txt', 'w')
for fn in fnMap.keys():
	s = '%s\t%d' % (fn, len(fnMap[fn]))
	print s.encode('gbk')
	su = s.encode('utf-8')
	fout.write(su + '\n')

json.dump(fnMap, file('iaf_first_names.json', 'w'))

#p1 = {}
#for k in fnMap.keys():
#    if len(fnMap[k]) == 1:
#        p1[k] = fnMap[k][0]

#json.dump(p1, file('iaf_unique_names.json', 'w'))
