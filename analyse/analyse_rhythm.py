#!/usr/bin/env python3
# *-* coding:utf8 *-*
import re
import sys
from pypinyin import pinyin, Style
sys.path.append('.')
import config


class Rhythm(object):
    def __init__(self):
        self.punc = config.punctuation
        self.punc_pattern = '[%s]+' % ''.join(self.punc)
        self.tone_pattern = re.compile('([a-z]+)([1-4])')

    def split(self, text):
        text_list = re.split(self.punc_pattern, text)
        text_list.remove('')
        return text_list

    def pinyin(self, text_list):
        pinyin_list = []
        shengdiao_list = []
        for text in text_list:
            for p in pinyin(text, style=Style.TONE3):
                m = self.tone_pattern.match(p[0])
                if m: # 阴平阳平上声去声
                    pinyin_list.append(m.group(1))
                    shengdiao_list.append(m.group(2))
                else: # 轻声
                    pinyin_list.append(p[0])
                    shengdiao_list.append('0')
        return pinyin_list, shengdiao_list

class RhythmAnalyser(object):
    def __init__(self, poet_file):
        self.rhythm = Rhythm()
        with open(poet_file) as f:
            self.poets = [line.strip() for line in f]

    def tones(self, sentence_list, shengdiao_list):
        idx = 0
        for sentence in sentence_list:
            start = idx
            end = idx + len(sentence)
            idx = end
            print(sentence)
            tone = [config.tone_map[x] for x in shengdiao_list[start:end]]
            print(''.join(tone))



    def analyse_poet(self, poet_text):
        sentence_list = self.rhythm.split(poet_text)
        pinyin_list, shengdiao_list = self.rhythm.pinyin(sentence_list)
        print(sentence_list, pinyin_list, shengdiao_list)
        self.tones(sentence_list, shengdiao_list)

    def analyse(self):
        for poet in self.poets[:10]:
            self.analyse_poet(poet)


if __name__ == '__main__':
    ra = RhythmAnalyser('poets_text/filter_poets_7.txt')
    ra.analyse()
