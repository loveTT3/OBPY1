# 装饰器的应用：登陆认证
'''
模拟登陆功能，装饰器的认证
'''

import json
from conf import settings
from lib import common

# 记录登陆状态
status_dicts={
    'username' : None,
    'status' : False
}

# 登陆
def login():
    username = input('请输入用户名')
    password = input('请输入密码')
    with open(user_path,mode='r',encoding='utf-8') as f:
        l = json.loads(f.read())
        if len(l) > 0:
            for i in range(len(l)):
                if l[i] == username: #检查账号是否存在
                    with open(user_path_np,mode='r',encoding='utf-8')as ff:
                        for i in ff:
                            d = json.loads(i.strip())
                            if list(d.keys())[0] == username: #字典的key转换为列表
                                if d[username] == password:
                                    print('登陆成功')
                                    status_dicts['status'] = True
                                    break
                                else:
                                    print('账号或者密码错误')
                                    break   
                        break    
                if i == len(l)-1:
                    print('账号不存在yayaay')
                    start()   
        else:
            print('账号不存在')    
            start()

# 注册
def register():
    username = input('请输入账号')
    password = input('请输入密码')
    user_d = {username:password}
    print(user_d)
    with open(user_path,mode='r',encoding='utf-8') as f:
        l1 = json.loads(f.read())
        print(l1,'l1的类型是：',type(l1),'长度是：',len(l1))
        if len(l1) > 0:
            for i in range(len(l1)):
                if l1[i] == username:
                    print('姓名重复')
                    register()
                    break
                if i == len(l1)-1: # 姓名不存在则添加
                    l1.append(username)
                    with open(user_path,mode='w',encoding='utf-8') as f:
                        f.write(json.dumps(l1))
                    zhuce(user_d) 
        else:
            # 直接添加，不进行判断
            with open(user_path,mode='w',encoding='utf-8') as f:
                print(l1)
                l1.append(username)
                f.write(json.dumps(l1))
                zhuce(user_d)

# 将账号密码写入user_np.txt
def zhuce(user_d):
    with open(user_path_np,mode='at',encoding='utf-8') as f:
        f.write(json.dumps(user_d))
        f.write('\n')
        print('注册成功')
        start()


# 注销函数
def zhuxiao():
    if status_dicts['status'] == True:
        status_dicts['status'] = False
        print('注销成功')
        start()
    else:
        print('您还未登陆，请重新选择')
        start()

#将usertxt初始化为一个空的列表
def zhuce_user():
    with open(user_path,mode='w',encoding='utf-8') as f:
        f.write(json.dumps([]))
        print('写入文件成功')

# 退出程序
def quit_():
    print('程序已退出')




@common.auth
def articel():
    print('欢迎访问文章界面')
    start()
@common.auth
def comment():
    print('欢迎访问评论界面')
    start()
@common.auth
def dariy():
    print('欢迎访问日记界面')
    start()

# articel() 
# comment()
# dariy()
# login()            
# register()
# articel()

dic_1= {
    1:login, # 登陆
    2:register, # 注册
    3:articel, #文章
    4:comment, # 评论
    5:dariy, # 日记
    6:zhuxiao, #注销
    7:quit_ #退出
}

# 操作栏
def start():
    n = input('请输入你的操作： 1-登陆 2-注册 3-文章界面 4-评论界面 5-日记界面 6-注销 7-退出').strip()
    i = int(n)
    dic_1[i]()
