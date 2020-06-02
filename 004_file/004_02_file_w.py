

# w模式
'''
四种文件分类主要四种模式：w，wb，w+，w+b
'''

# w
# 文件不存在 则创建为文件  再写入内容
f = open('a',encoding='utf-8',mode='w')
# f.write('嘤嘤嘤')
# 文件存在 清空文件内容 再写入内容
f.write('不再嘤嘤嘤')
f.close()

# wb
f1 = 












