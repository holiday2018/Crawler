# -*- coding:utf-8 -*-
"""
** 文件名: crawlermain.py
** 创建人: SunWiping<email:sunweiping2012@163.com>
** 日  期: 2015-07-21
** 描  述: 豆瓣电影的爬虫程序主模块
**
"""
import crawlerurl
import crawlersql
import crawlerregular


def main():
    crawlersql.create_table()
    comment_list = crawlerurl.get_movie_url()                  # 得到电影评论URL列表
    url = comment_list[2]
    print url
    comment_html = crawlerurl.get_comment_html(url)            # 得到评论页html文件
    comment = crawlerregular.CommentsParser()
    comment.feed(comment_html)                                  # 提取数据
    comments_all = comment.get_comments()                       # 返回提取结果
    comments_len = len(comments_all[0])
    input_sql = []
    for id_num in range(0, comments_len-1):
        input_sql.append(id_num)
        input_sql.append(comments_all[0][id_num])
        input_sql.append(comments_all[1][id_num])
        input_sql.append(comments_all[2][id_num])
        input_sql.append(comments_all[3][id_num])
        input_sql.append(comments_all[4][id_num])
        crawlersql.delete_data(id_num)
        print id_num
        print input_sql
        crawlersql.insert_table(input_sql)          # 将数据写入数据库
        input_sql = []                              # 清空数据缓存

if __name__ == '__main__':
    main()
