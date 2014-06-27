#!/usr/bin/env python
# -*- coding: UTF-8 -*-

import json
import re

f = file('iaf_map_clean1.json', 'r')
personMap = json.load(f)

personMap1 = {}
for k in personMap.keys():
    newk = k.upper()
    personMap1[newk] = personMap[k]

f = file('iaf_map_clean2.json', 'w')
json.dump(personMap1, f)
