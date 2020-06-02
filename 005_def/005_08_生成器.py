def fun():
    print(111)
    yield 3
    print(444)
    print(555)
    print(666)
    yield 4
ret = fun()
# print(type(ret))
# print(next(ret))



# yield与return的区别：
'''
return一般在函数中只设置一个，他的作用是终止函数，并且给函数的执行者返回值。
yield在生成器函数中可设置多个，他并不会终止函数，next会获取对应yield生成的元素。
'''


# yield from 可以直接把可迭代对象中的每一个数据作为生成器的结果进行返回
# yield from 是将列表中的每一个元素返回,所以 如果写两个yield from 并不会产生交替的效果
def func():
    list1 = [1,2,3,4,5]
    list2 = ['a','b','c','d','e']
    yield from list1
    yield from list2
g = func()

for i in g:
    print(i)