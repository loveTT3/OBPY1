

f = open('a',encoding='utf-8',mode='r+')
# read(n)
'''
1. 文件打开方式为文本模式时，代表读取n个字符
2. 文件打开方式为b模式时，代表读取n个字节
'''
print(f.read(1)) #

# seek()
'''
seek(n)光标移动到n位置,注意: 移动单位是byte,所有如果是utf-8的中文部分要是3的倍数
通常我们使用seek都是移动到开头或者结尾
移动到开头:seek(0)
移动到结尾:seek(0,2) seek的第二个参数表示的是从哪个位置进行偏移,默认是0,表示开头,1表示当前位置,2表示结尾
'''

# tell()
'''
使用tell()可以帮我们获取当前光标在什么位置
'''
print(f.tell())

# readable(),writeable()
print(f.readable())
print(f.writable())
f.close()