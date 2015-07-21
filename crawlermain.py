# -*- coding:utf-8 -*-
"""
** 文件名: crawler.py
** 创建人: SunWiping<email:sunweiping2012@163.com>
** 日  期: 2015-07-20
** 描  述: 豆瓣电影的爬虫程序主模块
**
"""
import crawlerurl
import crawlersql


def main():
    crawlersql.create_table()
    comment_list = crawlerurl.get_movie_url()                  # 得到电影评论URL列表
    url = comment_list[0]

    for id_num in range(1, 4):
        crawlersql.delete_data(id_num)
        name = "anny"+str(id_num)
        comment = crawlerurl.get_comment(url, id_num, name)
        crawlersql.insert_table(comment)


if __name__ == '__main__':
    main()
