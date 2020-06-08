# 模块

import time
def timee():
    print(time.time())


# __name__ 脚本方式运行时，返回固定字符串  __main__
# 以导入模块执行时  就是本模块名字
# print(__name__)

# 当前脚本执行  会立马执行可执行语句
# 以导入模块执行时，不执行可执行语句
def main():
    timee()

if __name__ == '__main__':
    main()