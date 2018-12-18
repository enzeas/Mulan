#!/usr/bin/env python3
# *-* coding: utf8 *-*
import os
import re
import json


def del_punc(text_line):
    text_line = re.sub('\[.+?\]', '', text_line.strip())
    text_line = re.sub('（.+?）', '', text_line)
    text_line = re.sub('[〔〕]', '', text_line)
    return text_line


poet_name = []
poet_author = []
poet_text = []
poet_page = []
poet_comment = []

poet_dir = 'poets/corpus/全唐詩'
poet_prefix = '卷'
json_poet = 'poets_json/quantangshi.json'

poet_files = os.listdir(poet_dir)
error_line = []

name = ''
author = ''
text = []
page = ''
comment = []

for poet_file in sorted(poet_files):
    if not poet_file.startswith(poet_prefix):
        continue
    full_name = poet_dir + os.sep + poet_file
    with open(full_name) as f:
        for line in f:
            if len(line) == 0:
                continue
            elif line.startswith('第'):
                poet_name.append(name)
                poet_author.append(author)
                poet_text.append(''.join(text))
                poet_page.append(page)
                poet_comment.append(''.join(comment))
                name = ''
                author = ''
                text = []
                page = ''
                comment = []
            elif line.startswith('　　　　'): # 全角空格
                arr = del_punc(line).split('　')
                if len(arr) != 2:
                    name = arr[0]
                    author = ''
                else:
                    name = arr[0]
                    author = arr[1]
            elif line.startswith('　　'): # 全角空格
                comment.append(del_punc(line))
            elif line.startswith('['):
                page = line.strip()
            else:
                text.append(del_punc(line))
poet_name.append(name)
poet_author.append(author)
poet_text.append(''.join(text))
poet_page.append(page)
poet_comment.append(''.join(comment))


poets = []
for idx, name in enumerate(poet_name):
    if idx == 0:
        continue
    poet = {
        'name': poet_name[idx],
        'author': poet_author[idx],
        'text': poet_text[idx],
        'page': poet_page[idx],
        'comment': poet_comment[idx],
    }
    poets.append(poet)
print("poets num: %d" % len(poets))

with open(json_poet, 'w') as f:
    json.dump(poets, fp=f, separators=(',', ': '), indent=2, ensure_ascii=False)
