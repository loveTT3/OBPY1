#动态参数

#动态参数分为两种:动态接受位置参数 *args，动态接收关键字参数**kwargs.


# *args 聚合为元组

def eat(*args):
    print(args)
    print('我请您吃：%s,%s,%s,%s' %args)
# eat('蒸羊羔','蒸熊掌','烧花鸭','烧雏鸡')

def num(*args):
    n = 0
    for i in args:
        n += i
    return n
# print(num(1,2,3,4,5))


#**args  聚合为字典
def func(**kwargs):
    print(kwargs)
# func(a = 1,b='的')


# 形参的顺序
# 位置参数  *args  默认参数  **kwargs
def sx(a,b,*args,sex='男',**kwargs):
    print(a,b)
    print(sex)
    print(args)
# sx(1,2,3,4,5,6,7,n = "嘤嘤嘤")

# 仅限关键字参数
# 位置参数  *args  默认参数  仅限关键字参数 **kwargs
def sx1(a,b,*args,sex='男',c,d,**kwargs):
    print(a,b)
    print(sex)
    print(c)
    print(d)
    print(args)
# sx1(1,2,3,4,5,6,c = 666,d =777,name='姓名')


#打散
s1 = 'alex'
l1 = [1, 2, 3, 4]
tu1 = ('武sir', '太白', '女神',)
def func1(*args):
    print(args) # ('a', 'l', 'e', 'x', 1, 2, 3, 4, '武sir', '太白', '女神')
# func(*s1,*l1,*tu1)

dic1 = {'name': '太白', 'age': 18}
dic2 = {'hobby': '喝茶', 'sex': '男'}
def func2(**kwargs):
    print(kwargs) # {'name': '太白', 'age': 18, 'hobby': '喝茶', 'sex': '男'}
# func2(**dic1,**dic2)


s1 = 'alex'
l1 = [1, 2, 3, 4]
tu1 = ('武sir', '太白', '女神',)
dic1 = {'name': '太白', 'age': 18}
dic2 = {'hobby': '喝茶', 'sex': '男'}
def funcn(*args,**kwargs):
    print(args) # ('a', 'l', 'e', 'x', 1, 2, 3, 4, '武sir', '太白', '女神')
    print(kwargs)
funcn(*s1,*l1,*tu1)
funcn(**dic1,**dic2)










