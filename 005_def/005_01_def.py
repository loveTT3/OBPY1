'''
# return
    1.在函数中，终止函数
    2.给返回值
        return后面写一个值  返回一个值
        return后面写多个值  返回的是元组
        return后面什么都不写 或者没有return   返回None
'''
def me():
    print(1)
    print(1)
    return
    print(2)
    print(2)    
# me()  


# 函数的参数
# 位置参数
def da(a,b):
    if str(a).isdigit() and str(b).isdigit() is True:
        if a > b:
            return a
        elif a == b:
            return '相等'
        else:
            return b
    else:
            return '输入不是数字'
print(da(2,23))

# 关键字参数
def da1(a,b):
    if str(a).isdigit() and str(b).isdigit() is True:
        if a > b:
            return a
        elif a == b:
            return '相等'
        else:
            return b
    else:
            return '输入不是数字'
# print(da(a = 2,b = 23))

# 混合参数 位置参数一定要在关键字参数前面
def da2(a,b):
    if str(a).isdigit() and str(b).isdigit() is True:
        if a > b:
            return a
        elif a == b:
            return '相等'
        else:
            return b
    else:
            return '输入不是数字'
# print(da(2,b = 23))

# 默认参数
def da3(a,b,c=4):
    return c 
print(da3(1,2,3))

# s1 = '2'
# # print(s1.isdigit())
# print(s1.isdecimal())


#三元运算符
# c = a if a > b else b