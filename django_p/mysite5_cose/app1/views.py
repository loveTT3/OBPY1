from django.shortcuts import render,HttpResponse,redirect

# Create your views here.
# 装饰器
def index_coo(f):
    def inner(request,*args,**kwargs):
        coo = request.COOKIES.get('k1')
        if coo == 'v1':
            ret = f(request,*args,**kwargs)
            return ret
        else:
            return redirect('index')
    return inner

# 登录
def index(request):
    method = request.method
    if method == 'GET':
        return render(request,'index.html')
    elif method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        # print(username,'=====',password)
        if username == '123' and password == '123':
            ret = redirect('home')
            # 增加cookies
            ret.set_cookie('k1','v1')
            # ret.set_signed_cookie('k1','v1',salt='加密盐', max_age=10,)# cookie过期时间，默认两周，单位秒，None代表cookie保留到关闭浏览器
            return ret
        else:
            return redirect('index')
            
# def home(request):
#     print(request.COOKIES)
#     coo = request.COOKIES.get('k1')
#     if coo == 'v1':
#         return render(request,'home.html')
#     else:
#         # return render(request,'index.html')
#         return redirect('index')

# 注销，清楚cookie
def logout(request):
    ret = render(request,'index.html')
    ret.delete_cookie('k1')
    return ret

# @index_coo
def home(request):
    return render(request,'home.html')



# session
def index2(request):
    method = request.method
    if method == 'GET':
        return render(request,'index2_session.html')
    elif method == 'POST':
        name = request.POST.get('username')
        password = request.POST.get('password')
        if name == '123' and password == '123':
            request.session["name"] = '123'
            return redirect('home2')
        else:
            return render(request,'index2_session.html')

def home2(request):
    cook = request.session.get('name')
    if cook == '123':
        return render(request,'home2_session.html')
    else:
        return redirect('index2')

def logout2(request):
    # 清除session
    request.session.flush()
    # request.session.delete()
    return redirect('index2')