# 文件的操作
# f = open(r'D:\测试文本.txt',encoding='utf-8',mode='r')
# msg = f.read()  #
# print(msg)
# f.close()



# 文件的读
'''
只读方式打开文件，文件的指针将会放在文件的开头。是文件操作最常用的模式，也是默认模式，
如果一个文件不设置mode，那么默认使用r模式操作文件。
'''
#r 模式
f = open(r'D:\测试文本.txt',encoding='utf-8',mode='r')
# msg = f.read()  # 将文件全部读取出来 但很占用内存
# msg = f.read(3) #置顶读取到什么位置 按字符读取
# msg = f.readline()  # 每次读取一行 但后面会有\n
# msg1 = f.readline().strip()  # 光标在第二行开头,且后面没有了换行
# print(f.readlines())

# for循环 不占内存 按行读取
for i in f:
    print(i.strip())

# print(msg)
# print(msg1)
f.close()



#rb模式
'''
带b的都是以二进制的格式操作文件，他们主要是操作非文字文件：图片，音频，视频等,
并且如果你要是带有b的模式操作文件，那么不用声明编码方式。
'''
f = open(r'D:\测试图片.png',mode='r')
print(f.read())
f.close()







