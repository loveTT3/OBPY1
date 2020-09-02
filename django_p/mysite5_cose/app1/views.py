from django.shortcuts import render,HttpResponse,redirect

# Create your views here.
# 装饰器
def index_coo(f):
    def inner(request,*args,**kwargs):
        coo = request.COOKIES.get('k1')
        if coo == 'v1':
            ret = f(request,*args,**kwargs)
        else:
            return redirect('index')
    return inner


def index(request):
    method = request.method
    if method == 'GET':
        return render(request,'index.html')
    elif method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        print(username,'=====',password)
        if username == '123' and password == '123':
            ret = redirect('home')
            # 增加cookies
            ret.set_cookie('k1','v1')
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


@index_coo
def home(request):
    return render(request,'home.html')