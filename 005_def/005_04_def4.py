

# 默认参数的陷阱
'''
如果默认参数是可变的数据类型，那么无论调用多少次这个默认参数，都是同一个
'''

def fun(a,list1=[]):
    list1.append(a)
    return list1
# print(fun(10,))
# print(fun(20,[]))
# print(fun(100,))

def fun1(a,list1=[]):
    list1.append(a)
    return list1
r1 = fun1(10,)
r2 = fun1(20,[])
# r3 = fun1(100,)
# print(r1)  #[10,100]
# print(r2)  #[20]
# print(r3)


