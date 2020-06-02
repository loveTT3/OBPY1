# f-strings格式化输出
'''
结构就是F(f)+ str的形式，在字符串中想替换的位置用{}展位，
与format类似，但是用在字符串后面写入替换的内容，而他可以直接识别。
'''

name = '猪八戒'
msg = F'姓名:{name}{name}'
# print(msg)


# 添加表达式
name1 = 'Berry'
msg1 = f'姓名：{name1.upper()}'  # 全部大写
print(msg1)

# 字典 列表
dict1 = {'name': 'Tom', 'age': 12}
list1 = ['Tom', 18]
msg2 = f'姓名：{dict1["name"]} 年纪{dict1["age"]}'
# print(msg2)
msg3 = f'姓名：{list1[0]} 年纪{list1[1]}'
# print(msg3)


# 函数也可以
def add_a_b(a, b):
    return a + b
a = 1
b = 2
print('求和结果' + f'{add_a_b(a, b)}')

# 多行F
s = f'姓名：{name} '\
    f'小名：{name1} '\
    f'年纪：{list1[1]}'
print(s)












