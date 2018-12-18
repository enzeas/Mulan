#!/usr/bin/env python3
# *-* coding: utf8 *-*
import re
import json


poet_name = []
poet_author = []
poet_type = []
poet_text = []

origin_poet = 'poets/corpus/唐詩三百首.txt'
json_poet = 'json/tangshisanbaishou.json'

with open(origin_poet) as f:
    for line in f.readlines():
        arr = line.strip().split(':')
        if len(arr) != 2:
            continue
        if arr[0] == '詩名':
            poet_name.append(arr[1])
        elif arr[0] == '作者':
            poet_author.append(arr[1])
        elif arr[0] == '詩體':
            poet_type.append(arr[1])
        elif arr[0] == '詩文':
            text = re.sub('\(.+?\)', '', arr[1])
            poet_text.append(text)
            assert (len(poet_name) == len(poet_author) and
                    len(poet_author) == len(poet_type) and
                    len(poet_type) == len(poet_text))

poets = []
for idx in range(len(poet_name)):
    poet = {
        'name': poet_name[idx],
        'author': poet_name[idx],
        'type': poet_type[idx],
        'text': poet_text[idx],
    }
    poets.append(poet)
print("poets num: %d" % len(poets))

with open(json_poet, 'w') as f:
    json.dump(poets, fp=f, separators=(',', ': '), indent=2, ensure_ascii=False)



