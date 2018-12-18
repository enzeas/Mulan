#!/usr/bin/env python3
# *-* coding:utf8 *-*
import json
import os
import re
import sys

# 过滤出五言诗和七言诗

class Filter(object):
    def __init__(self, num):
        self.num = num
        self.punc = ['，', '。', '？', '！', '：', '、', '【', '】', ]
        self.pattern = '[%s]+' % ''.join(self.punc)

    def _split_text(self, text):
        return re.split(self.pattern, text)

    def filter(self, text):
        segs = self._split_text(text)
        for seg in segs:
            if len(seg) == 0:
                continue
            if len(seg) != self.num:
                return False
        return True

class PoetFilter(object):
    def __init__(self, num):
        self.filter = Filter(num)

    def init_file(self, file_name):
        with open(file_name) as f:
            self.poets = json.load(f)

    def run(self):
        filtered = filter(lambda x: self.filter.filter(x['text']), self.poets)
        return [p['text'] for p in filtered]


def main(num=7):
    poet_dir = 'poets_json'
    filter_poets = []
    pf = PoetFilter(num)
    for file_name in os.listdir(poet_dir):
        full_name = poet_dir + os.sep + file_name
        pf.init_file(full_name)
        filter_poets.extend(pf.run())
    filter_poets_name = 'poets_text/filter_poets_%d.txt' % num
    with open(filter_poets_name, 'w') as f:
        for poet_text in filter_poets:
            f.write(poet_text)
            f.write('\n')

if __name__ == '__main__':
    if len(sys.argv) > 1:
        main(int(sys.argv[1]))
    else:
        main()
