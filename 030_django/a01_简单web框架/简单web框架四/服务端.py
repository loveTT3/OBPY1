# import socket
# from threading import Thread
import time
from wsgiref.simple_server import make_server
from jinja2 import Template


def html1():
    data_tag = str(time.time())
    print(data_tag)
    with open(r'OBPY1\030_django\a01_简单web框架\简单web框架四\test.html',
              mode='r',
              encoding='utf-8') as f:
        data = f.read()
    # 字符串替换 实现动态
    data = data.replace('$xxoo$', data_tag)

    dic1 = {'name':'孙悟空','age':19}
    # dic1 = {1:{'name':'孙悟空','age':19},2:{'name':'孙悟空','age':19}}
    # for k,v in dic1.items():
    #     for k1,v1 in v.items():
    #         print(k1)
    #         print(v1)
    tem = Template(data) # 生成模板文件
    data = tem.render({'userinfo':dic1}) # 把数据填充到模板里面
    
    data = data.encode('utf-8')
    return data

def css1():
    with open(r'OBPY1\030_django\a01_简单web框架\简单web框架四\test.css',
              mode='rb') as f:
        data = f.read()
    return data

def js1():
    with open(r'OBPY1\030_django\a01_简单web框架\简单web框架四\test.js',
              mode='rb') as f:
        data = f.read()
    print(data)
    return data

def min_css():
    with open(r'OBPY1\030_django\a01_简单web框架\简单web框架四\bootstrap-3.3.7-dist\css\bootstrap.min.css',
              mode='rb') as f:
        data = f.read()
    # print(data)
    return data

urlpatterns = [('/', html1), ('/test.css', css1), ('/test.js', js1),('/bootstrap-3.3.7-dist/css/bootstrap.min.css',min_css)]

# wsgiref本身就是个web框架，提供了一些固定的功能（请求和响应信息的封装，不需要我们自己写原生的socket了也不需要咱们自己来完成请求信息的提取了，提取起来很方便）
#函数名字随便起
def application(environ, start_response):
    '''
    :param environ: 是全部加工好的请求信息，加工成了一个字典，通过字典取值的方式就能拿到很多你想要拿到的信息
    :param start_response: 帮你封装响应信息的（响应行和响应头），注意下面的参数
    :return:
    '''
    start_response('200 OK', [('k1','v1'),])
    # print(environ)
    # print(environ['PATH_INFO'])  #输入地址127.0.0.1:8000，这个打印的是'/',输入的是127.0.0.1:8000/index，打印结果是'/index'   
    path = environ['PATH_INFO']    
    print(path)

    for i in urlpatterns:
        if path == i[0]:
            # i[1](conn)
            ret = i[1]()
            break
    else:
        ret = b'404 not found'


    return [ret]

#和socketserver那个模块很像啊
httpd = make_server('127.0.0.1', 8080, application)
print('Serving HTTP on port 8080...')
# 开始监听HTTP请求:
httpd.serve_forever()