
# 在不改变原被装饰的函数的源代码以及调用方式下，为其添加额外的功能。


import time
def index():
    time.sleep(2)
    print('欢迎步入星光大道')
# index()  #执行

def timer(f):
    def inner():
        start_time = time.time()
        f()
        end_time = time.time()
        print(f'时间为{end_time - start_time}')
    return inner
# timer(index)() 
# index = timer() # 执行
# index()#执行



# 有返回值的时候 装饰器怎么写
def index1():
    time.sleep(2)
    print('欢迎步入星光大道')
    return '嘤嘤嘤'
# print('原先的东西',index1())

def timer1(f):
    def inner():
        s_time = time.time()
        ff = f()
        e_time = time.time()
        print(f'时间：{e_time- s_time}')
        return ff
    return inner
# index1 = timer1(index1)
# print(index1())



# 有参数的装饰器     
'''标准版 格式'''
# def wrapper(func):
#     def inner(*args,**kwargs):
#         '''执行被装饰函数之前的操作'''
#         ret = func
#         '''执行被装饰函数之后的操作'''
#         return ret
#     return inner
def time2(f):
    def inner(n):
        s_time = time.time()
        f(n)
        e_time = time.time()
        print(f'执行时间{e_time-s_time}')
    return inner
# index2 = time2(index2)
# index2('朱八戒')
# print(time2(index2).__code__.co_freevars)

@time2   # 等于 index2 = time2(index2)
def index2(name):
    time.sleep(2)
    print(f'欢迎来到{name}的家')
index2('猪八戒')




# # 标准版装饰器  代码优化  语法糖，在需要装饰器的函数上一行加上  @{函数名}
def wrapper(f):
    def inner(*args,**kwargs):
        ret = f(*args,**kwargs)
        return ret
    return inner













