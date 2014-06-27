#!/usr/bin/env python
# -*- coding: UTF-8 -*-

import json
import re

f = file('iaf_en_names_clean2.json', 'r')
personMap1 = json.load(f)
print len(personMap1)

f = file('iaf_en_names1_clean1_upper.json', 'r')
personMap2 = json.load(f)
print len(personMap2)

personMap3 = {}
for k in personMap1:
    personMap3[k] = personMap1[k]
    
for k in personMap2:
    if k not in personMap3:
        personMap3[k] = personMap2[k]
    elif personMap2[k] != personMap3[k]:
        print 'bad', k

f = file('iaf_en_names2_merged_upper.json', 'w')
json.dump(personMap3, f)
print len(personMap3)
