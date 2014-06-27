#!/usr/bin/env python
# -*- coding: UTF-8 -*-

import json
import re
import sys

f = file(sys.argv[1], 'r')
personMap = json.load(f)

names = personMap.keys()
print len(names)

#cmp=lambda x,y: len(x) - len(y)
names.sort()

fout = file(sys.argv[2], 'w')
for n in names:
    s = n.encode('utf-8')
    fout.write(s + '\n') # str(len(n))
