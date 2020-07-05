# object 类  是所有类的父类
# 所有python3中的类都继承object类

# isinstance

class foo1:
    pass

class son1(foo1):
    pass

c = son1()
print(type(c) is son1)     # True
print(type(c) is foo1)     # False
print(isinstance(c,son1))  # True
print(isinstance(c,foo1))  # True


# 类调用函数  就是函数
# 对象调用   就是方法

print(son1.__base__)
print(son1.__name__)


