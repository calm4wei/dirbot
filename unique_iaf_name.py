#!/usr/bin/env python
# -*- coding: UTF-8 -*-

import json
import re
import sys

f = file('iaf_names.txt', 'r')
persons = f.readlines()
fnMap = {}
for p in persons:
    n = p.decode('utf-8')
    mo = re.match(u'^(.*)·.*$', n)
    
    if fnMap.has_key(u'珊莎'):
        print '-------->', fnMap[u'珊莎']
        
    if mo:
        fn = mo.group(1)
        if fnMap.has_key(fn):
            if fnMap[fn]:
                fnMap[fn] = fnMap[fn].append(n)
            else:
                print 'bad', fn, fnMap[fn]
                fnMap[fn] = [n]
                sys.exit(1)
        else:
            print 'adding ', fn
            fnMap[fn] = [n]
            #print fnMap[fn]

        if fnMap.has_key(fn):
            if fnMap[fn]:pass
                #print fn, len(fnMap[fn])
            else:
                print 'bad: ', fn
                print '-------->', fnMap[u'珊莎']
                sys.exit(1)

p1 = {}
for k in fnMap.keys():
    if len(fnMap[k]) == 1:
        p1[k] = fnMap[k][0]

persons = json.dump(p1, file('iaf_unique_names.json', 'w'))
