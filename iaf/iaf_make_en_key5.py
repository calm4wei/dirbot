#!/usr/bin/env python
# -*- coding: UTF-8 -*-

import json
import re

f = file('iaf_last_names.json', 'r')
personMap = json.load(f)

personMap1 = {}
for k in personMap.keys():
    newk = k.upper();
    vs = personMap[k];
    vs1 = []
    for v in vs:
        v = v.upper()
        vs1.append(v)
    personMap1[newk] = vs1

f = file('iaf_last_names1.json', 'w')
json.dump(personMap1, f)
