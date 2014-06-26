#!/usr/bin/env python
# -*- coding: UTF-8 -*-

import json
import re

f = file('items7.json', 'r')
persons = json.load(f)
r = {}
for p in persons:
    r[p['name']] = {'url':p['url'], 'description':p['description']}
fout = file('items7map.json', 'w')
persons = json.dump(r, fout)