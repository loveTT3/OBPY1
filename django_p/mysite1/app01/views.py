from django.shortcuts import render
from django.shortcuts import HttpResponse

# Create your views here.

# 登录界面
# url(r'^login/', views.login),
def login(request):
    method = request.method
    # 根据方法不同 确定是请求界面 还是 表达提交
    if method == 'GET':
        return render(request,'login.html')
    elif method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        if username == '123'  and password =='123':
            return HttpResponse('登陆成功')
        else:
            return HttpResponse('登陆失败')

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


def base(request):
    return render(request,'base.html')