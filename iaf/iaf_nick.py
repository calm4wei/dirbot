#!/usr/bin/env python
# -*- coding: UTF-8 -*-

import json
import re
import sys

f = file('iaf_nick.txt', 'r')
nicks = f.readlines()

personMap1 = {}
for k in nicks:
    k = k.strip().decode('utf-8')
    t = k.split('\t')
    if len(t) == 2:
        n = t[0].strip()
        nn = t[1].split('|')
        for nick in nn:
            nick = nick.strip()
            personMap1[nick] = n
            print nick, n

f = file('iaf_nick.json', 'w')
json.dump(personMap1, f)
