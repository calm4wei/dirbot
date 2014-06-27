#!/usr/bin/env python
# -*- coding: UTF-8 -*-

import json
import re
import sys

op = sys.argv[1] #first or last
fn = sys.argv[2]
fnout1 = sys.argv[3]
fnout2 = sys.argv[4]

f = file(fn, 'r')
persons = json.load(f)
f.close()

fnMap = {}
for p in persons:
    n = p.strip()
    exp = ur'^([^\s]*)\s+.*$'
    if op == 'last':
        exp = ur'^.*\s+([^\s]+)$'
    mo = re.match(exp, n)
    
    if mo:
        fn = mo.group(1)
        if op == 'first' and (fn.upper() == 'THE' or fn.upper() == 'A'):
		    continue

        if fnMap.has_key(fn):
            fnMap[fn].append(n)
        else:
            fnMap[fn] = [n]

countL = [(len(fnMap[fn]), fn) for fn in fnMap]
countL.sort(None, None, True)
    
fout = file(fnout1, 'w')
for (cnt, fn) in countL:
	s = '%s\t%d' % (fn, cnt)
	print s
	fout.write(s + '\n')

json.dump(fnMap, file(fnout2, 'w'))
