# sys
# 和python解释器相关的操作



#获取命令行
import sys

# 返回的是字符串  
# print('脚本名：' ,sys.argv[0])
# print('第一个参数：' ,sys.argv[1])
# print('第二个参数：' ,sys.argv[2])

print(int(sys.argv[1])+int(sys.argv[2]))