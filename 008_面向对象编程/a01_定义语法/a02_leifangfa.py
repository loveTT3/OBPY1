from math import pi
class cirle:
    def __init__(self,r):
        self.r = r

    def zhouchang(self):
        zc = self.r * 2 * pi
        print(zc)
    def mianji(self):
        mj = self.r **2 * pi
        print(mj)

c1 = cirle(10)
c1.zhouchang()
c1.mianji()



# 统计 类被实例化了多少次
class A:
    count = 0
    def __init__(self):
        A.count +=1
        # print(A.count)

a = A()
a1 = A()
a2 = A()
print(A.count)