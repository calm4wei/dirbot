#!/usr/bin/env python
# -*- coding: UTF-8 -*-

import json
import re
import sys

f = file('iaf_en_names_clean1.json', 'r')
persons = json.load(f)
f.close()

fnMap = {}
for p in persons.keys():
    n = p.strip()
    mo = re.match(ur'^([^\s]*)\s+.*$', n)
    
    if mo:
        fn = mo.group(1)
        if fn == 'the' or fn == 'The' or fn == 'A' or fn == 'a':
		    continue

        if fnMap.has_key(fn):
            fnMap[fn].append(n)
        else:
            fnMap[fn] = [n]

fout = file('en_first_name_count.txt', 'w')
for fn in fnMap.keys():
	s = '%s\t%d' %(fn, len(fnMap[fn]))
	print s
	fout.write(s + '\n')

json.dump(fnMap, file('iaf_en_first_names.json', 'w'))
