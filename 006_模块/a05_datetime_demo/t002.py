# datatime模块
import datetime
now_time = datetime.datetime.now()  # 现在的时间
# 只能调整的字段：weeks days hours minutes seconds
print(datetime.datetime.now() + datetime.timedelta(weeks=3)) # 三周后
print(datetime.datetime.now() + datetime.timedelta(weeks=-3)) # 三周前
print(datetime.datetime.now() + datetime.timedelta(days=-3)) # 三天前
print(datetime.datetime.now() + datetime.timedelta(days=3)) # 三天后
print(datetime.datetime.now() + datetime.timedelta(hours=5)) # 5小时后
print(datetime.datetime.now() + datetime.timedelta(hours=-5)) # 5小时前
print(datetime.datetime.now() + datetime.timedelta(minutes=-15)) # 15分钟前
print(datetime.datetime.now() + datetime.timedelta(minutes=15)) # 15分钟后
print(datetime.datetime.now() + datetime.timedelta(seconds=-70)) # 70秒前
print(datetime.datetime.now() + datetime.timedelta(seconds=70)) # 70秒后


current_time = datetime.datetime.now()
# 可直接调整到指定的 年 月 日 时 分 秒 等

print(current_time.replace(year=1977))  # 直接调整到1977年
print(current_time.replace(month=1))  # 直接调整到1月份
print(current_time.replace(year=1989,month=4,day=25))  # 1989-04-25 18:49:05.898601

# 将时间戳转化成时间
print(datetime.date.fromtimestamp(1232132131))  # 2009-01-17