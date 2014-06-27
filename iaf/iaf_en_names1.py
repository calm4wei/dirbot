#!/usr/bin/env python
# -*- coding: UTF-8 -*-
# 原来的提取正则提取到了最后一个括号里的内容
# 现在提取有多个括号，所有括号里的内容
# 并区分，第1个是正式名，后面的多个是昵称

import json
import re

f = file('iaf_map_clean2.json', 'r')
personMap = json.load(f)

names = personMap.keys()

enNames = {}
enNames1 = {}
for n in names:
    v = personMap[n]
    mos = re.findall(u'（([^（）]*)）', v['description'])
    c = 0
    if len(mos) > 1:
        for mo in mos:
            c = c+1
            en = mo.strip()
            en = en.replace(u'\xa0', ' ')
            
            if c == 1:
                enNames[en] = {'isnick':False, 'name':n}
            else:
                enNames[en] = {'isnick':True, 'name':n}

            enNames1[en] = n
            print en, n.encode('gbk', 'ignore')

print len(enNames)

f = file('iaf_en_names1.json', 'w')
json.dump(enNames1, f)

f = file('iaf_en_names1_with_nickflag.json', 'w')
json.dump(enNames, f)
