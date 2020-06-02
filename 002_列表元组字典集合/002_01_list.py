# 列表
#有序 有索引  可切片

list1 = [1,'dss',True,[1,2,3],2,3,4]
#索引
for i in list1:
    print(i,type(i))
#切片
print(list1[1:2])
print(list1[::2])


#创建
l1 = [1,2,3,'dsa']
l2 = list('12dsa3221')   #拆分之后当成每一个元素
print(l2)
l3 = [i for i in range(3)]  #列表推导式
print(l3)


ll = ['s','b','nec']
#增 三种方法
ll.append('med')  # 追加
ll.insert(1,'插入的数据')   #插入
ll.extend('abcd')       #迭代增加一组数据,组成当前对象的最小元素
ll.extend(['22'])
print(ll)   #['s', '插入的数据', 'b', 'nec', 'med', 'a', 'b', 'c', 'd', '22']

#删 
ll.pop(1)  # 按照索引删除(返回的是删除的元素)
ll.pop()  #默认删除最后一个元素
ll.remove('b')  #只删第一个匹配到的元素
del ll[2] # 按照索引删除
del ll[0:2]
# ll.clear()  #清空列表
print(ll)

#改
l2 = [1,2,3,'a','b','c']
l2[0] = 'ca'
l2[1:2] = 'ddsadsa'   #不加步长任一添加，加步长必须一一对应
print(l2)


#列表的嵌套
'''
l1 = [1, 2, 'taibai', [1, 'WuSir', 3,]]
1, 将l1中的'taibai'变成大写并放回原处。
2，给小列表[1,'alex',3,]追加一个元素,'老男孩教育'。
3，将列表中的'alex'通过字符串拼接的方式在列表中变成'alexsb'
'''
l3 = [1,'aaa',3,['a','v','c']]
l3[1] = l3[1].upper()
l3[3].append('s')
l3[3].append('ss')
l3[3][1] = l3[3][1]+'拼接的'
print('l3是什么： ',l3)



l1 = [13, 2,5 ,'taibai', [1, 'WuSir', 3,]]
# count
print(l1.count(1))  # 元素出现次数
# index
print(l1.index(2))  # 元素索引 找不到报错

l2 = [28,3,544]
#sort
l2.sort() #将列表排序，从小到大
print(l2)
l2.sort(reverse = True)  # 将列表排序 从大到小
print(l2)

#reverse
l2.reverse()    #列表翻转
print(l2)

# 列表相加
l1 = [1,2,3,'a']
l2 = [3,2,1]
print(l1+l2)
print(l2 * 3)



# l1 = [11, 22, 33, 44, 55]，请把索引为奇数对应的元素删除
# 直接删除
l1 = [11, 22, 33, 44, 55,66,77,88,99]
del l1[1:len(l1):2]
print(l1)
# 倒叙删索引
l1 = [11, 22, 33, 44, 55,66,77,88,99]
for  i in range(len(l1)-1,-1,-1):
    if i % 2 == 1:
        l1.pop(i)
print(l1)
# 将所有索引为偶数的元素 组成新的列表
l1 = [11, 22, 33, 44, 55,66,77,88,99]
l2 = []
for i in range(len(l1)):
    if i % 2 == 0:
        l2.append(l1[i])
print(l2)

