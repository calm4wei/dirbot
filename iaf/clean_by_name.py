#!/usr/bin/env python
# -*- coding: UTF-8 -*-

import json
import re

f = file('iaf_map_clean.json', 'r')
persons = json.load(f)
print len(persons)

f = file('iaf_names.txt', 'r')
names = f.readlines()
print len(names)

persons1 = {}
for n in names:
    n = n.strip().decode('utf-8')
    print n
    persons1[n] = persons[n]

print len(persons1)
f = file('iaf_map_clean1.json', 'w')
json.dump(persons1, f)
