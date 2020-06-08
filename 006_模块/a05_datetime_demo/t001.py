#  datetime模块  
# 封装了一些和日期时间相关的类
'''
date
time
datetime
timedelta
'''
import datetime

# date对象
d = datetime.date(2010,12,11)
print(d)
# 获取date对象的各个属性
print(d.day,d.year,d.month)


# time对象
t = datetime.time(12,23,45)
print(t)
# 获取属性
print(t.hour,t.minute,t.second)


# timedelta  主要用于 计算
print(datetime.datetime(2022,11,11,11,11,11))
print(datetime.datetime.now())

r = datetime.timedelta(hours=1)
tr = d+r
print(tr)