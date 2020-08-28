from django.shortcuts import render,HttpResponse
from django.http import JsonResponse
# Create your views here.

def login(request):
    method = request.method
    if method == "GET":
        return render(request,'login.html')
    elif method == "POST":
        name = request.POST.get('username')
        password = request.POST.get('password')
        print(name,password)
        if  name == '' or password == '':
            return JsonResponse(1,safe=False) #safe字段为false，可以将任何类型转换为json  值为true则只能穿字典，否则TypeError报错
        elif int(name) == 123 and int(password) == 123:
            # print(111)
            # return render(request,'base.html')
            return JsonResponse(3,safe=False)
        else:
            return JsonResponse(2,safe=False)
    # return render(request,'login.html')


def base(request):
    return render(request,'base.html')

# 局部刷新  返回的不是界面 
def ajax_add(request):
    i1 = int(request.GET.get('i1'))
    i2 = int(request.GET.get('i2'))
    ret = i1+i2
    # print(ret)
    return JsonResponse(ret, safe=False)
