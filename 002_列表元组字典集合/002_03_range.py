#类似于列表   可以自定义数字范围


r = range(1,12,3)
rr = range(100,1,2)
for i in r:
    print(i,end=' ')
print()
# 有索引

ll = ['wq',1,2,3,4,5]

for i in range(0,len(ll)):
    print(ll[i],end=' ')



# enumerate 枚举 将索引和值组成序列
l = [1,2,3,4,5,6,7,1,1]

for i,v in enumerate(l,2):
    print(i,v)

for i in enumerate(l,2):
    print(i)
