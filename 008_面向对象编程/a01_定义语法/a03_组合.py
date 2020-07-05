# 类的组合
# 一个类的对象是另一个类的属性

class banji:
    def __init__(self,curse):
        self.curse = curse
class kecheng:
    def __init__(self,name,zhouqi,peace):
        self.name = name
        self.zhouqi = zhouqi
        self.peace = peace

b1 = banji('linux57')
b2 = banji('python22')
k1 = kecheng('linux','22天',123) 
k2 = kecheng('python','33天',234) 

b1.curse = k1
print(b1.curse.zhouqi)


# 组合的作用