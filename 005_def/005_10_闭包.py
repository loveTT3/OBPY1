#

# 闭包
# 保存局部信息不被销毁  保证数据的安全性


#完成一个计算不断增加的系列值的平均值的需求。
# l = []
# def make_avg(new_value):
#     l.append(new_value)
#     total = sum(l)
#     avggg = total/len(l)
#     return avggg
# print(make_avg(100))
# print(make_avg(200))
# print(make_avg(400))
# print(make_avg(400))



# 闭包
def m_avg():
    # ll和avg函数  就是闭包
    ll = []  # ll为自由变量
    def avg(value1):
        ll.append(value1)
        summ = sum(ll)
        av = summ/len(ll)
        return av
    return avg
ttl = m_avg()
print(ttl(1000))
print(ttl(2000))


# 闭包的定义：
#     1. 闭包是嵌套在函数中的函数。
#     2. 闭包必须是内层函数对外层函数的变量（非全局变量）的引用。
# 闭包的作用：
#     1.保存局部信息不被销毁，保证数据的安全性。
# 闭包的应用：
#     1.可以保存一些非全局变量但是不易被销毁、改变的数据。
#     2.装饰器。

# 查看是否有自由变量  侧面反映是否是闭包函数
print(ttl.__code__.co_freevars) # 查看函数的自由变量
print(ttl.__code__.co_varnames) # 查看函数的局部变量
print(avg.__code__.co_freevars)


