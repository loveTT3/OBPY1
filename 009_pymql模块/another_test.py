# 删改查


import pymysql

# 1.连接并打开Mysql数据库
conn = pymysql.connect(
    host='127.0.0.1',  #主机地址，若是自己的主机也可以用'localhost'
    port=3306,  #端口
    user='root',  #用户
    password='root',  #密码
    database='bzbh',  #数据库
    charset='utf8',  # 设置编码，此处不能写utf-8
    # autocommit=True  # 自动提交
)


# 2.创建游标，获取游标对象 ----> 游标 可以用来提交sql命令
# cur = conn.cursor()   # 将查询出来的结果制作成元祖的形式返回
cur2 = conn.cursor(cursor = pymysql.cursors.DictCursor) # 将查询出来的结果制作成字典的形式返回

# 3.通过execute()方法可以执行sql语句
try:

    cur2.execute('==sql语句 增删改==')
    conn.commit() #写入数据库
except expression as identifier:
    # 如果sql语句有问题  那么回滚回之前状态  不写入
    conn.rollback()



