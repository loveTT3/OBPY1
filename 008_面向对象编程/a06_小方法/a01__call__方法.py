# 对象能不能运行  即对象() 
# 对象加() 调用这个类中的__Call__方法


class A:
    def __call__(self,*args,**kwargs):
        print('---')
obj = A()
print(callable(obj))  #看看对象能不能运行


class B:
    pass
obj2 = B()
print(callable(obj2))
