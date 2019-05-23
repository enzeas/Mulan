#!/usr/bin/env python
# *-* coding: utf8 *-*
import os
import re
import json
import xml.etree.ElementTree as ET


def del_punc(text_line):
    text_line = re.sub('\n', '', text_line.strip())
    text_line = re.sub('[【】]', '', text_line)
    return text_line


filename = 'poets/longyusheng.org/唐宋名家词选.xml'
json_poet = 'poets_json/tangsongci.json'

ci_list = []
data = open(filename, encoding='utf-16').read()
root = ET.fromstring(data)
for ci in root:
    if ci.tag != '名家词':
        continue
    id = ci.attrib['id']
    author = id
    for info in ci:
        author_ci = {}
        #print(info.tag, info.attrib, info.text)
        if info.tag == '作家':
            author = info.text
        elif info.tag == '词':
            for detail in info:
                if detail.tag == '词牌':
                    author_ci['cipai'] = detail.text
                if detail.tag == '正文':
                    for child in detail:
                        if child.tag == '段落':
                            author_ci['text'] = del_punc(child.text)
            author_ci['author'] = author
            ci_list.append(author_ci)

with open(json_poet, 'w') as f:
    json.dump(ci_list, fp=f, separators=(',', ': '), indent=2, ensure_ascii=False)
