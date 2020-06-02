# 函数名的运用
# 函数名是一个特殊的变量，他除了具有变量的功能，还有最主要一个特点就是加上()就执行，其实他还有一个学名叫第一类对象。


# 1.函数的内存地址
'''
函数名指向的是这个函数的内存地址
函数的内存地址()是执行这个函数的关键
'''
def fun():
    print(666)
# print(fun,type(fun))

# 2.函数名可以赋值给其他变量
a = fun
# a()


# 3.函数名可以当做其他容器的变量
def fun1():
    print('第一个')
def fun2():
    print('第二个')
def fun3():
    print('第三个')
list1 = [fun1,fun2,fun3]
# for i in list1:
    # i()


# 4.函数名可以当做函数的参数
def f1():
    print('fff1')
def f2(f):
    print('fff2')
    f()
# f2(f1)


# 5.函数名可以作为函数的返回值
def f11():
    print('fff1')
def f22(f):
    print('fff2')
    return f
ret = f22(f11)
ret()




