from django.shortcuts import render
from django.shortcuts import HttpResponse

# Create your views here.
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