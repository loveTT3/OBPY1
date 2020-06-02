#赋值  
# 指向同一个地址
'''
l1 = [1,2,3,'qw']
l2 = l1
l1.append('new')
print(l1)
print(l2)
print(l1 is l2)
'''

# import copy
# # 浅copy
# l1 = [1,2,3,'qw',['a','b']]
# # l2 = l1.copy()
# l2 = copy.copy(l1)
# l1.append('new')
# l1[0] = 'zsmj'
# l1[4].append('666')
# print(l1)
# print(l2)
# print(l1 is l2)


#  深copy
import copy
l1 = [1,2,'a',['p',2]]
l2 = copy.deepcopy(l1)
l1.append('new')
l1[3].append('嘤嘤嘤')
# l1[0] = 6
print(l1[0],l2[0],l1[0] is l2[0])
print(l1)
print(l2)
print(l1 is l2)

