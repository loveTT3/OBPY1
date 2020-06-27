# 登陆注册小程序

'''
需求描述：
    注册：将用户名密码加密之后写入文件
    登陆：将用户名密码鱼文件中的对比，匹配成功则登陆成功
    退出：结束
'''
import hashlib

def jiami(username,password):
    m = hashlib.md5()
    m.update(username.encode('utf-8'))
    m.update(password.encode('utf-8'))
    res = m.hexdigest()
    # print('加密的： ',res)
    return res

def zhuce(username,password):
    res = jiami(username,password)
    with open('login.txt',mode='at',encoding='utf-8') as f:
        f.write(res)
        f.write('\n')

def denglu(username,password):
    res = jiami(username,password)
    # print('登录产生的：',res)
    with open('login.txt',mode='rt',encoding='utf-8') as f:
        for line in f:
            # print('文件读的： ',line)
            if line.strip() == res:
                return True
        else:
            return False

while True:
    op = int(input('输入操作：1：注册 2：登陆 3：退出'))
    if op == 1:
        username = input('请输入用户名：')
        password = input('请输入密码')
        zhuce(username,password)
    elif op == 2:
        username = input('请输入登陆同户名：')
        password = input('请输入登陆密码：')
        res = denglu(username,password)
        if res:
            print(f'登陆成功，欢迎 {username}')
        else:
            print('登陆失败，用户名或密码不正确')
    elif op == 3:
        print('再见')
        break
