#!/usr/bin/python
# -*- coding: UTF-8 -*-

import MySQLdb

# 打开数据库连接
db = MySQLdb.connect("localhost", "root", "200888", "longgetest", charset="utf8mb4")

# 使用cursor()方法获取操作游标
cursor = db.cursor()
cursor.execute('SET NAMES utf8;')
cursor.execute('SET CHARACTER SET utf8mb4;')
cursor.execute('SET character_set_connection=utf8mb4;')


sql = """INSERT INTO TieBaList(user_id,
             is_membertop, is_multi_forum, vid, tie_href, reply_num,
             is_good, is_top, is_protal,
             frs_tpoint, is_bakan, author_name, title, first_post_id)
             VALUES ('4933031972', 'None', 'None', '', 'http://tieba.baidu.com/p/4933031972', '68', 'None', 'True', 'None', 'None', 'None', '爆机人脉，没有人脉你和谁谈单👿', '【公告】暂行吧规-发帖尺度规定', '102370371223')"""

print sql
try:
   # 执行sql语句
   cursor.execute(sql)
   # 提交到数据库执行
   db.commit()
except(IOError, ZeroDivisionError), e:
   # Rollback in case there is any error
   print "数据库执行出错：", e
   # Rollback in case there is any error
   db.rollback()

# 关闭数据库连接
db.close()

