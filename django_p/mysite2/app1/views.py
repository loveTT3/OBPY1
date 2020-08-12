from django.shortcuts import render,redirect,HttpResponse
import datetime
# Create your views here.
def login(request):
    name = 'bo而且企鹅无群二b'
    age = 14321321
    l1 = [23,'dsa','时间',22]
    d1 = {'name':'dds','age':23}

    class Dog:
        def __init__(self):
            self.kind = 'dog'
        def eat(self):
            return '嘤嘤嘤'
    dog = Dog()

    
    now = datetime.datetime.now()
    words = 'i love you '
    tag = '<a href="http://www.baidu.com">百度</a>'

    # return render(request,'index.html',{'name':name,'age':age,'d1':d1,'l1':l1,'dog':dog})
    # locals 返回当前所有的变量
    return render(request,'index.html',locals())

def tags(request):
    l1 = [1,2,3,'a','b','c']
    dic1 = {'name':'BOb','age':23,'yyy':'','hobby':['eat','drink','high']}
    return render(request,'tags.html',{'l1':l1,'dic1':dic1})

# 用于模板继承
def muban(request):
    return render(request,'muban.html')
def jicheng1(request):
    return render(request,'m_jicheng1.html')
def jicheng2(request):
    return render(request,'m_jicheng2.html')
def jicheng3(request):
    return render(request,'m_jicheng3.html')

# 用于静态文件 和 自定义标签
def test(request):
    s1 = '孙悟空'
    return render(request,'test.html',{'s1':s1})

# 用于测试组件
def zujian(request):
    return render(request,'zujian2.html')