#!/usr/bin/env python
# -*- coding: UTF-8 -*-

import json
import re
import sys

f = file('iaf_en_names_clean.json', 'r')
persons = json.load(f)
f.close()

fout = file('iaf_en_names.txt', 'w')
names = persons.keys()
names.sort()
for p in names:
    fout.write(p.encode('utf-8') + '\n')