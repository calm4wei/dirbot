#!/usr/bin/env python
# -*- coding: UTF-8 -*-

import json
import re

f = file('iaf_map_clean.json', 'r')
personMap = json.load(f)

names = personMap.keys()
#names = list(set(names))
print len(names)

cmp=lambda x,y: len(x) - len(y)
names.sort(cmp)

fout = file('iaf_names.txt', 'w')
for n in names:
    s = n.encode('utf-8')
    fout.write(s + '\n') # str(len(n))
