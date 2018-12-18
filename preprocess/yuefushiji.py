#!/usr/bin/env python3
# *-* coding: utf8 *-*
import re
import json


poet_name = []
poet_page = []
poet_dynasty = []
poet_author = []
poet_volume = []
poet_text = []
poet_comment = []

origin_poet = 'poets/corpus/樂府詩集.txt'
json_poet = 'poets_json/yuefushiji.json'

comment = ''
with open(origin_poet) as f:
    for line in f:
        arr = line.strip().split('：', 1)
        if len(arr) != 2:
            continue
        if arr[0] == '詩題':
            poet_name.append(arr[1])
        elif arr[0] == '篇目':
            poet_page.append(arr[1])
        elif arr[0] == '朝代':
            poet_dynasty.append(arr[1])
        elif arr[0] == '作者':
            poet_author.append(arr[1])
        elif arr[0] == '卷別':
            poet_volume.append(arr[1])
        elif arr[0] == '詩題解':
            comment = arr[1]
        elif arr[0] == '詩文':
            text = re.sub('\(.+?\)', '', arr[1])
            poet_comment.append(comment)
            comment = ''
            poet_text.append(text)
            assert (len(poet_name) == len(poet_page) and
                    len(poet_page) == len(poet_dynasty) and
                    len(poet_dynasty) == len(poet_author) and
                    len(poet_author) == len(poet_volume) and
                    len(poet_volume) == len(poet_comment) and
                    len(poet_comment) == len(poet_text))


poets = []
for idx, name in enumerate(poet_name):
    poet = {
        'name': poet_name[idx],
        'page': poet_page[idx],
        'dynasty': poet_dynasty[idx],
        'author': poet_author[idx],
        'volume': poet_volume[idx],
        'comment': poet_comment[idx],
        'text': poet_text[idx],
    }
    poets.append(poet)
print("poets num: %d" % len(poets))

with open(json_poet, 'w') as f:
    json.dump(poets, fp=f, separators=(',', ': '), indent=2, ensure_ascii=False)
