#!/usr/bin/env python
# -*- coding: UTF-8 -*-

import json
import re
import sys

f = file('iaf_en_names_clean.json', 'r')
enMap = json.load(f)
f.close()

f = file('iaf_en_names.txt', 'r')
names = f.readlines()
f.close()

enMap1 = {}
for n in names:
    print n
    n = n.strip()
    enMap1[n] = enMap[n]

fout = file('iaf_en_names_clean1.json', 'w')
json.dump(enMap1, fout)

