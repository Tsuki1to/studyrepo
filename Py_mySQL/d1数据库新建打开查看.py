# 开发时间：29/9/2022 下午10:55
#连接MysQL（socket）

import pymysql
conn = pymysql.connect(host='127.0.0.1', port=3306, password='zyt950908', charset="utf8",

                       )
cursor = conn.cursor()

#1.查看数据库
#发送指令
cursor.execute("show databases")
#获取指令的结果
result = cursor.fetchall()
print(result)


