# __new__方法

class A:
    def __new__(cls,*args,**kwargs):
        print('构造方法')
        o = super().__new__(cls)
        return o
    def __init__(self):
        print('init')

A()