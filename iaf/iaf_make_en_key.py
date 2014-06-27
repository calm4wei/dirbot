#!/usr/bin/env python
# -*- coding: UTF-8 -*-

import json
import re

f = file('iaf_en_names_clean1.json', 'r')
personMap = json.load(f)

personMap1 = {}
for k in personMap.keys():

f = file('iaf_en_names_clean2.json', 'w')
json.dump(enNames, f)
