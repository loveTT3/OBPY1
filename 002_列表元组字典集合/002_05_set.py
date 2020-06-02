#集合  set
#无序   元素不可重复   元素不可变
setset = set()

set1 = {1,2,'e','ef',False}
set2 = {'1',1,2,'ww',True}
print(set1)

#增
set1.add('新增')    #追加元素
set1.update('迭代')    #迭代增加
print(set1)
#删
set1.remove(1)  #按照元素删除
set1.pop()  #随机删除   
print(set1)



set11 = {1,2,'e','ef',False}
set22 = {'1',1,2,'ww','第三'}
#交
print(set11 | set22)


# 对列表去重，直接将列表变为集合即可
l1 = [1,1,2,2,3,3,'da','ds','da']
s1 = set(l1)
print(s1)
