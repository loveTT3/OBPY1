'''
1. 文件a.txt内容：每一行内容分别为商品名字，价钱，个数。

apple 10 3

tesla 100000 1

mac 3000 2

lenovo 30000 3

chicken 10 3

通过代码，将其构建成这种数据类型：
[{'name':'apple','price':10,'amount':3},{'name':'tesla','price':1000000,'amount':1}......] 并计算出总价钱。
'''

with open('a',encoding='utf-8',mode='r') as f:   
    f.seek(0,2)
    num = f.tell()
    f.seek(0)
    list1 = []
    while True:
        if f.tell() == num:
            break
        else:
            aa = f.readline().strip()
            # print(aa)
            a = aa.split(' ')
            # print(a)    #每行列表
            if len(a) > 1:
                d = dict({'name':a[0],'price':int(a[1]),'amount':int(a[2])})
                list1.append(d)
print(list1)
num = 0
for i in range(len(list1)):
    num += list1[i]['price'] * list1[i]['amount']
print(num)


