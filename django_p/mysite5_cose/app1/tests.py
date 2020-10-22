from django.test import TestCase

# Create your tests here.
# 标准版装饰器
def wrapper(func):
    def inner(*args,**kwargs):
        '''执行被装饰函数之前的操作'''
        ret = func
        '''执行被装饰函数之后的操作'''
        return ret
    return inner


def wrapper1(func):
    def inner(r):
        '''执行被装饰函数之前的操作'''
        ret = func(r)
        '''执行被装饰函数之后的操作'''
        return ret
    return inner

@wrapper1  # pp = wrapper(pp)  返回 inner
def pp(r):
    print(r,123)


pp(0000)