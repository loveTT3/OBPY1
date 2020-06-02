

# 列表推导式
# 用一行代码构建一个比较复杂有规律的列表


# list1 = []
# for i in range(4):
#     list1.append(i)
# print(list1)

'''
列表推导式：
    1.循环模式：[变量(加工的变量) for 变量 in iterable]
    2.筛选模式：[变量(加工的变量) for 变量 in iterable if 条件]
'''
# 循环模式
l1 = [i*i for i in range(1,11)] #10以内整数的平方写入列表
print(l1)
l2 = [i for i in range(2,11,2)] #10以内所有偶数写入列表
print(l2)
l3 = [f'python{i}' for i in range(1,11)] # python1-python10写入列表 
print(l3)

# 筛选模式
l4 = [i for i in range(1,21) if i % 3 == 0] # 30以内被三整除的数
print(l4)
#过滤掉长度小于3的字符串列表，并将剩下的转换成大写字母
ll = ['wusir', 'laonanhai', 'aa', 'b', 'taibai']
ll1 = [i.upper() for i in ll if len(i) > 3] 
print(ll1)
# 找到嵌套列表中名字含有两个‘e’的所有名字
names = [['Tom', 'Billy', 'Jefferson', 'Andrew', 'Wesley', 'Steven', 'Joe'],
         ['Alice', 'Jill', 'Ana', 'Wendy', 'Jennifer', 'Sherry', 'Eva']]
for i in names:
    for nn in i:
        nn.count('e') > 2
for i in names:
    for nn in range(len(i)):
        i[nn].count('e') >2
ss = [i[nn] for i in names for nn in range(len(i)) if i[nn].count('e') >=2 ]
print(ss)
s = [nn for i in names for nn in i if nn.count('e') >=2 ]
print(s)





# 生成器表达式
gen = (i ** 2 for i in range(10))
print(gen)
print(gen.__next__())
# 获取1-100内能被3整除的数
gen = (i for i in range(1,100) if i % 3 == 0)
for num in gen:
    print(num)

'''
生成器表达式和列表推导式的区别:
    列表推导式比较耗内存,所有数据一次性加载到内存。而生成器表达式遵循迭代器协议，逐个产生元素。
    得到的值不一样,列表推导式得到的是一个列表.生成器表达式获取的是一个生成器
    列表推导式一目了然，生成器表达式只是一个内存地址。
'''


# 字典推导式
lst1 = ['jay','jj','meet']
lst2 = ['周杰伦','林俊杰','郭宝元']
dic = {lst1[i]:lst2[i] for i in range(len(lst1)) }
print(dic)

# 集合推导式
lst = [1,2,3,-1,-3,-7,9]
s = {abs(i) for i in lst}
print(s)

