# -*- coding:utf-8 -*-
"""
** 文件名: crawler.py
** 创建人: SunWiping<email:sunweiping2012@163.com>
** 日  期: 2015-07-22
** 描  述: 豆瓣电影的爬虫程序的网页数据抓取模块
**
"""
import urllib


def get_movie_url():
    """get all movie url"""
    douban_url = "http://movie.douban.com/"
    content = urllib.urlopen(douban_url).read()
    movie_list = []                                      # 存放最终获取的电影URL地址
    show = 0
    while show is not -1:
        show = content.find(r'=showing', show+1)
        movie_url = content[show-46:show+8]
        comment_url = movie_url[:-13] + "comments"
        movie_list.append(comment_url)
    movie_list = list(set(movie_list))
    return movie_list


def get_comment(url, id_num, name):
    comment = urllib.urlopen(url).read()
    comment_text = """
    记忆中的小时代没有这么差啊，看在最后一集的份上给个3.5吧，毕竟最后那个苏打绿的《我好想你》的mv剪辑的不错
    """
    comment_list = [id_num, name, 1, 37, comment_text, "2015-07-22"]
    return comment_list



