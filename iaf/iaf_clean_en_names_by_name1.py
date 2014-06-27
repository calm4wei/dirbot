#!/usr/bin/env python
# -*- coding: UTF-8 -*-

import json
import re
import sys

f = file('iaf_en_names1.json', 'r')
enMap = json.load(f)
f.close()

f = file('iaf_en_names1_with_nickflag.json', 'r')
enMap_nick = json.load(f)
f.close()

f = file('iaf_en_names1.txt', 'r')
names = f.readlines()
f.close()

enMap1 = {}
enMap1_nick = {}
for n in names:
    print n
    n = n.strip()
    enMap1[n] = enMap[n]
    enMap1_nick[n] = enMap_nick[n]
    

fout = file('iaf_en_names1_clean1.json', 'w')
json.dump(enMap1, fout)

fout = file('iaf_en_names1_withnickflag_clean1.json', 'w')
json.dump(enMap1_nick, fout)

print len(enMap1)
