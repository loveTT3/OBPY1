#终止循环
flag = True
while flag:
    print('嘤嘤嘤')
    print('awsl')
    flag = False


#输出0~100
n = 1
while n < 10:
    print(n)
    n = n + 1     


#输出 0+1+2+...+100
s = 0
l = 1
while l < 10:
    s = s + l
    l = l + 1
print(s)


#break 结束本次循环
flag1 = True
while flag1:
    print(11)
    print(22)
    break
    print(33)
    flag= False


#1~100所有偶数
m = 0
while m < 10:
    if m%2 == 0:
        print(m)
    m = m +1


#continue  结束当前循环 继续下次循环
m = 0
while m < 10:
    if m%2 == 0:
        print(m)
    m = m +1
    continue
    print(m)


#while else
#while 被break打断  则不执行else的语句
count = 1
while count < 5:
    print(count)
    if count == 2:
        break
    count = count + 1
else:
    print(666)


























