#!/usr/bin/env python
# -*- coding: UTF-8 -*-

import json
import re
import sys

op = sys.argv[1] #first or last
lng = sys.argv[2] #en or cn
fn = sys.argv[3]
fnout1 = sys.argv[4]
fnout2 = sys.argv[5]

f = file(fn, 'r')
persons = f.readlines()
f.close()

fnMap = {}
for p in persons:
    n = p.strip().decode('utf-8')
    exp = ''
    if lng == 'en':
        exp = ur'^([^\s]*)\s+.*$'
        if op == 'last':
            exp = ur'^.*\s+([^\s]+)$'
        mo = re.match(exp, n)
    elif lng == 'cn':
        exp = ur'^([^·]*)·.*$'
        if op == 'last':
            exp = u'^.*·([^·]+)$'
        mo = re.match(exp, n)
    
    
    if mo:
        fn = mo.group(1)
        if op == 'first' and (fn.upper() == 'THE' or fn.upper() == 'A'):
		    continue

        if op == 'last' and lng == 'cn' and (fn[-1] == u'世'):
		    fn = fn[:-2]

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
	fout.write(s.encode('utf-8') + '\n')

json.dump(fnMap, file(fnout2, 'w'))
