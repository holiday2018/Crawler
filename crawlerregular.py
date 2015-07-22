# -*- coding:utf-8 -*-
"""
** 文件名: crawlerregular.py
** 创建人: SunWiping<email:sunweiping2012@163.com>
** 日  期: 2015-07-21
** 描  述: 豆瓣电影的爬虫程序的正则表达式模块
**
"""
import re


class CommentsParser():
    def __init__(self):
        self.comments = []

    def feed(self, data):
        names = []
        stars = []
        dates = []
        texts = []

        name = re.findall(r'''people(\s*)([\S]*)(\s*)class="">([\S]*)</a>''', data, re.S | re.I)
        for n in name:
            names.append(n[3])
        self.comments.append(names)
        # print names

        star = re.findall(r'''rating"(\s*)title="([\S]*)">''', data, re.S | re.I)
        for s in star:
            stars.append(s[1])
        self.comments.append(stars)
        # print stars

        useful = re.findall(r'''votes pr5">(\d+)''', data, re.S | re.I)
        self.comments.append(useful)
        # print useful

        text = re.findall(r'''<p class="">(\s)(.*)''', data,  re.I)
        for t in text:
            texts.append(t[1])
        self.comments.append(texts)
        # print texts

        date = re.findall(r'''([\s]+)(\d+)-(\d+)-(\d+)''', data, re.S | re.I)
        for d in date:
            dates.append(d[1]+d[2]+d[3])
        self.comments.append(dates)
        # print dates

    def get_comments(self):
        return self.comments
