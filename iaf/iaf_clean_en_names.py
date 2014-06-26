#!/usr/bin/env python
# -*- coding: UTF-8 -*-

import json
import re
import sys

f = file('iaf_en_names.json', 'r')
persons = json.load(f)
f.close()

names = persons.keys()
for p in names:
    mo = re.match(r'^(.*)\((.*)\)$', p)
    if mo:
        v = persons.pop(p)
        newn1 = mo.group(1).strip()
        newn2 = mo.group(2).strip()
        print newn1, '=', newn2
        persons[newn1] = v
        persons[newn2] = v

fout = file('iaf_en_names_clean.json', 'w')
json.dump(persons, fout)

