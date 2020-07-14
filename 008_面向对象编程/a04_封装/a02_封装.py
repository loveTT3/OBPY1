#什么是封装

#广义：把属性和方法封装起来，外面不能直接调用，比如类里面的属性和方法

# 狭义：把属性和方法封装起来，外面不能调用，只能内部使用
# 所有私有的内容 只能在类的内部使用
class User:
    def __init__(self,name,passwd):
        self.usr = name
        self.__pwd = passwd  # 加上双下划线，变成私有的实例变量
    def get_pwd(self):
        return self.__pwd
 