#!/usr/bin/env python
# -*- coding: UTF-8 -*-

import json
import re
import sys

fn = sys.argv[1]
fnout = sys.argv[2]

f = file(fn, 'r')
personMap = json.load(f)

personMap1 = {}
for k in personMap.keys():
    newk = k.upper();
    vs = personMap[k]
    if isinstance(vs, list):
        personMap1[newk] = [v.upper() for v in vs] # 列表解析
    else:
        personMap1[newk] = vs.upper()

f = file(fnout, 'w')
json.dump(personMap1, f)
