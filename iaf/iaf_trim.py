#!/usr/bin/env python
# -*- coding: UTF-8 -*-

import json
import re

f = file('items7.json', 'r')
persons = json.load(f)
r = {}
for p in persons:
	p['name'] = p['name'].strip()
    p['description'] = p['description'].strip()
    p['url'] = p['url'].strip()
fout = file('items7_1.json', 'w')
persons = json.dump(persons, fout)
