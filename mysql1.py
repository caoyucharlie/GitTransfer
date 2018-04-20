# 该代码为连接服务器/本地mysql数据库，并对数据库进行操作
import pymysql
'''
连接阿里云服务器里的database，host为ip地址，user是database名字，passwd为1221
选择database名字为 SRS，端口默认为3306
'''
db = pymysql.connect(
    host='127.0.0.1',
    user='root',
    passwd='1221',
    db='SRS',
    port=3306, charset='utf8'
)
# 获取游标，开辟一个缓冲区，用于存放sql语句执行的结果
cursor = db.cursor()
# 插入， 三个引号可以换行
try:
    # 执行sql
    sql = '''insert into tbcourse values
    (8888, 'mysql数据库',3,'从删除到跑路')'''

    cursor.execute(sql)
# 提交
    db.commit()
except:
    db.rollback()

    # 获取结果
data = cursor.fetchall()
print(data)
# 关闭连接
db.close()
