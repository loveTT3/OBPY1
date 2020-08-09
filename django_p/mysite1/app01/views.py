from django.shortcuts import render
from django.shortcuts import HttpResponse
from django.shortcuts import redirect

# Create your views here.

# 登录界面
# url(r'^login/', views.login),
def login(request):
    method = request.method
    # 根据方法不同 确定是请求界面 还是 表达提交
    if method == 'GET':
        print('================================request请求的方法')
        print('请求方法', request.method)
        print('请求的 GET参数的类字典对象',request.GET)
        print('请求的 POST参数的类字典对象',request.POST)
        print('请求体',request.body)
        print('请求头',request.META)
        print('========================================')
        return render(request,'login.html')
    elif method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        if username == '123'  and password =='123':
            # return HttpResponse('登陆成功')
            # 登陆成功，重定向到首页
            return redirect('/base/')
        else:
            return HttpResponse('登陆失败')

# 装饰器
def wrapper(fn):
    def inner(request,*args,**kwargs):
        print('xxxxx')
        ret = fn(request)
        print('xsssss')
        return ret
    return inner



# 首页（用于登陆重定向 ）
def base(request):
    return render(request,'base.html')

# CBV
from django.views import View
from django.utils.decorators import method_decorator
class base1(View):
    # 使用CBV时要注意，请求过来后会先执行dispatch()这个方法，如果需要批量对具体的请求处理方法，如get，post，手动改写dispatch方法，这个dispatch方法就和在FBV上加装饰器的效果一样。
    # def dispatch(self, request, *args, **kwargs):
    #     print('before')
    #     obj = super().dispatch(request, *args, **kwargs)
    #     print('after')
    #     return obj
    
    #装饰器 需导包 特殊写法
    @method_decorator(wrapper)
    def get(self,request):
        print('进入界面了')
        return render(request,'base.html')
    def post(self,request):
        pass



# 年份路径   /boks/2002
def year_books(request,year):
    print(year)
    return HttpResponse(year)
# 月份带年份 /books/2002/22
def year_month_books(request,year,month):
    print(year,'--',month)
    return HttpResponse(year,'--',month)


# app01的首页 /app01/
def app01_base(request):
    return render(request,'app01_base.html')
