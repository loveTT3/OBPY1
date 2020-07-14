
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


sql = 'select * from where user = %s and password = %s'
cur = conn.cursor()
# 防止sql注入，传参数用execute来传
cur.execute(sql,(user,pwd))
