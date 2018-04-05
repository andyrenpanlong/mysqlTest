#!/usr/bin/python
# -*- coding: UTF-8 -*-

import MySQLdb

# 打开数据库连接
db = MySQLdb.connect("localhost", "root", "200888", "iocommunet")

# 使用cursor()方法获取操作游标
cursor = db.cursor()

# SQL 查询语句
sql = "SELECT * FROM TieBaList"
try:
   # 执行SQL语句
   cursor.execute(sql)
   # 获取所有记录列表
   results = cursor.fetchall()
   print len(results)
   for row in results:
      print row[5]
   #    fname = row[0]
   #    lname = row[1]
   #    age = row[2]
   #    sex = row[3]
   #    income = row[4]
   #    # 打印结果
   #    print "fname=%s,lname=%s,age=%d,sex=%s,income=%d" % \
   #           (fname, lname, age, sex, income )
except:
   print "Error: unable to fecth data"

# 关闭数据库连接
db.close()