# 把一个方法伪装成一个属性，在调用时不用加（）
# property 装饰的方法不能有参数
class Goods:
    discount = 0.8
    def __init__(self,name,origin_price):
        self.name = name
        self.__price = origin_price
    @property
    def price(self):
        return self.__price * self.discount
    @price.setter
    def price(self,new_value):
        print('调用我啦')
        if isinstance(new_value,int):
            self.__price = new_value
    @price.deleter
    def price(self):
        del self.__price

apple = Goods('apple',5)
print(apple.price)  #调用的是@property装饰的price
apple.price = 'sda'    #调用的是@price.setter装饰的price
print(apple.price)
apple.price = 10    #调用的是@price.setter装饰的price
print(apple.price)

# del apple.price
# print(apple.price)