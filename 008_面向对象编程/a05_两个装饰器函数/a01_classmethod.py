

# 定义了一个方法，默认传了self 但是这个self没有被使用


class Goods:
    __discount = 0.8
    def __init__(self):
        self.__price = 5
        self.price = self.__price * self.__discount
    @ classmethod  # 把一个对象绑定的方法 修改成一个类方法
    def change_discount(cls,new_value):
        cls.__discount = new_value

Goods.change_discount(0.6)  # 类方法可以通过类名和对象名调用
apple = Goods()
print(apple.price)

# 什么时候用
    # 定义了一个方法，默认传了self 但是这个self没有被使用
    # 并且你在这个方法里用到了当前的类名，或者准备使用这个类的内存空间中的名字的时候



