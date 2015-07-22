# -*- coding:utf-8 -*-
"""
** 文件名: crawlersql.py
** 创建人: SunWiping<email:sunweiping2012@163.com>
** 日  期: 2015-07-21
** 描  述: 豆瓣电影的爬虫程序中的MySQL操作模块
**
"""
import MySQLdb

# 数据库名称
DATABASE_NAME = ''
# host = 'localhost' or '172.0.0.1'
HOST = ''
# 端口号
PORT = ''
# 用户名称
USER_NAME = ''
# 数据库密码
PASSWORD = ''
# 数据库编码
CHAR_SET = ''


# 初始化参数
def init():
    global DATABASE_NAME
    DATABASE_NAME = 'movie_comment'
    global HOST
    HOST = 'localhost'
    global PORT
    PORT = '3306'
    global USER_NAME
    USER_NAME = 'root'
    global PASSWORD
    PASSWORD = 'root123'
    global CHAR_SET
    CHAR_SET = 'utf8'


# 获取数据库连接
def get_conn():
    init()
    return MySQLdb.connect(host=HOST, user=USER_NAME, passwd=PASSWORD, db=DATABASE_NAME, charset=CHAR_SET)


# 获取cursor
def get_cursor(conn):
    return conn.cursor()


# 关闭连接
def conn_close(conn):
    if conn != None:
        conn.close()


# 关闭cursor
def cursor_close(cursor):
    if cursor is not None:
        cursor.close()


# 关闭所有
def close(cursor, conn):
    cursor_close(cursor)
    conn_close(conn)


# 创建表
def create_table():

    sql = '''
    CREATE TABLE `comment` (

    `id` int(11) NOT NULL,
    `name` varchar(40) NOT NULL,
    `starnum` varchar(8) DEFAULT NULL,
    `usefulnum` int(11) DEFAULT NULL,
    `comment` varchar(200) DEFAULT NULL,
    `comment_date` varchar(11) NOT NULL,
    PRIMARY KEY (`id`),
    UNIQUE KEY `name` (`name`)

    ) ENGINE=InnoDB DEFAULT CHARSET=utf8
    '''
    conn = get_conn()
    cursor = get_cursor(conn)
    cursor.execute("DROP TABLE IF EXISTS COMMENT")
    result = cursor.execute(sql)
    conn.commit()
    close(cursor, conn)
    return result


# 查询表信息
def query_table(table_name):
    if table_name != '':
        sql = 'select * from ' + table_name
        conn = get_conn()
        cursor = get_cursor(conn)
        result = cursor.execute(sql)
        for row in cursor.fetchall():
            print(row)
            # for r in row:      #循环每一条数据
                #print(r)
        close(cursor, conn)
    else:
        print('table name is empty!')


# 插入数据
def insert_table(comment_list):
    sql = 'insert into comment(id, name, starnum, usefulnum,comment, comment_date ) values(%s,%s, %s, %s, %s, %s)'
    params = (comment_list[0], comment_list[1], comment_list[2], comment_list[3], comment_list[4], comment_list[5])
    conn = get_conn()
    cursor = get_cursor(conn)
    result = cursor.execute(sql, params)
    conn.commit()
    close(cursor, conn)
    return result


# 更新数据
def update_table():
    sql = 'update comment set name = %s where id = 1'
    params = ('红孩儿')
    conn = get_conn()
    cursor = get_cursor(conn)
    result = cursor.execute(sql, params)
    conn.commit()
    close(cursor, conn)
    return result


# 删除数据
def delete_data(id_num):
    sql = 'delete from comment where id = %s'
    params = (id_num)
    conn = get_conn()
    cursor = get_cursor(conn)
    result = cursor.execute(sql, params)
    conn.commit()
    close(cursor, conn)
    return result


# 数据库连接信息
def print_info():
    print('数据库连接信息:' + DATABASE_NAME+' '+ HOST+' '+ PORT +' '+  USER_NAME +' '+  PASSWORD +' '+  CHAR_SET)


# 打印出数据库中表情况
def show_databases():
    sql = 'show databases'
    conn = get_conn()
    cursor = get_cursor(conn)
    cursor.execute(sql)
    for row in cursor.fetchall():
        print(row)


# 数据库中表情况
def show_tables():
    sql = 'show tables'
    conn = get_conn()
    cursor = get_cursor(conn)
    cursor.execute(sql)
    for row in cursor.fetchall():
        print(row)
