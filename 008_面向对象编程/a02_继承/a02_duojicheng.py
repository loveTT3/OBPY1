# 多继承

# 哪个父类写在前面，优先找哪个
class foo1:
    def __init__(self):
        pass
    def fun(self):
        print('foo1  fun')

class foo2:
    def __init__(self):
        pass
    def fun(self):
        print('foo2 fun')

class son(foo2,foo1):
    pass

c = son()
c.fun()