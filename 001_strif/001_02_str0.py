#字符串

s1 = 'as'
s2 = "ss"
#三引号：用于换行的字符串
s3 = '''鹅鹅鹅 
曲项向天歌
白毛浮绿水
红掌拨清波'''

print(s3)
#字符串可以拼接 相乘
print(s3 * 2)
print(s1 + s2)

#判断变量数据类型
print(type(s2))

#input  出来的全部是字符串类型
# s4 = input('输入姓名：')
# print(s4)




#切片(索引，索引，步长)
str1 = 'python全栈课程'
#按照索引取值
str2 = str1[0]
print(str2)
print(str1[-1])
#按照切片取值
str3 = str1[0:6] #包前不包后
str4 = str1[6:] 
print(str3+ '  ' + str4)
#有步长
str5 = str1[:5:2]
#倒序
str6 = str1[-1:-6:-2]
print(str6)
#全取
print(str1[:])
print(str1[::-1]) #倒序





#字符串操作方法
# 对字符串的任何操作 都是产生一个新的字符串 
s1 = 'ssbTTaa'
#upper  lower  大写小写  
# 中文自动忽略 
print(s1.upper())
print(s1.lower())

#startswith  endswith    以什么开始结束
print(s1.startswith('s',1))     # 从索引1开始
print(s1.endswith('T',3,5))    # 从索引3开始到索引5

#replace  替换
print(s1.replace('s','c',1))

#strip  去除首尾的空白或字符
str2 = '33ddfssd '
print(str2.strip())
str3 = str2.strip('3')
print(str3)

# split  切割  默认按空格分割
# 返回列表
s1 = '23 dd sad  ds  '
print(s1.split())
print(s1.split('d'))
print(s1.split('d',2))

# join 连接
s2 = 'alsd'
s3 = '+'.join(s2)
print(s3,type(s3))

# count  某个字符出现的次数
ss = 'sdajjirjiidjiajsakvnnskamvbjfjks ndjnksndla'
print(ss.count('a'))

# formate  格式化输出
msg = '我叫{},今年{},性别{}'.format('悟空',23,'男')
msg1 = '我叫{0},今年{1},性别{2},爱我{0}吗'.format('悟空',23,'男')
msg2 = '我叫{name},今年{age},性别{sex}'.format(name='悟空',age=23,sex='男')
print(msg)
print(msg1)
print(msg2)

#is 系列
name = '11wddef11'
print(name.isalnum())   #是不是由字母和数字组成  
print(name.isalpha())   #只由字母组成
print(name.isdecimal())   #只由十进制组成


# captalize swapcase
name = 'llwwEE2'
print(name.capitalize())    #首字母大写，其余全部变成小写
print(name.swapcase())  #大小写翻转
msg = 'wo ai ni '
print(msg.title())  # 每个单词的首字母大写
s = 'berry'
print(s.center(20)) # 内容居中，总长度 空白填充
print(s.center(20,'+'))

# find index
name = 'llwwEE2'
print(name.find('w',1,4))   #返回元素索引  找不到返回-1
print(name.index('w',1,4))  #返回元素索引  找不到报错