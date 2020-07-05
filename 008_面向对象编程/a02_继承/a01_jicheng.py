# 继承

# 子类可以直接使用父类的方法和静态变量
# 子类和父类方法重名的时候，执行子类的函数  
#如果有重名 还想用父类的方法，则 父类名.方法名(self)
class Animal:
    def __init__(self,name):
        self.name = name
    def eat(self):
        print('%s is eating' %self.name)

class Cat(Animal):
    def __init__(self,name,sex):
        self.sex = sex
        Animal.__init__(self,name)
    def pa(self):
        print('%s pa'%self.name)
    def eat(self): 
        print('子类的方法')   
        Animal.eat(self)

c = Cat('miao','man')
print(c.__dict__)
c.pa()
c.eat()