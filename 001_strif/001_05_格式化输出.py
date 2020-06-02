#格式化输出
# msg = '''----个人简介----
# Name: Bob
# Age : 187
# job : sb
# sex : boy
# ----------------
# '''
# print(msg)


#格式化输出 %占位符  s--->str  d--> i--> r-->
# name = input('请输入你的姓名')
# age = input('请输入你的年龄')
# job = input('请输入你的工作')
# sex = input('请输入你的性别')
# msg = '''----%s个人简介----
# Name: %s
# Age : %s
# job : %s
# sex : %s
# ----------------
# '''%(name,name,age,job,sex)
# print(msg)


# 格式化输出中，只想表示一个百分号 而不是作为占位符使用
# 再加一个百分号
ms = '我的名字%s，学习了1%%的python'%('Jerry')
print(ms)
