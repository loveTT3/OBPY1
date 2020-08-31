from django.shortcuts import render,HttpResponse
from django.http import JsonResponse
import os
from mysite4_ajax import settings    
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

# 上传图片
def file_sc(request):
    method = request.method
    # print('方法',method)
    if method == 'GET':
        return render(request,'file_sc.html')
    else:
        # print(request.POST)
        # file_obj = request.FILES.get('p1')
        file_obj = request.FILES.get('p_name')
        
        print('名字是',file_obj,type(file_obj))
        
        path = os.path.join(settings.BASE_DIR,'static\img',file_obj.name)
        print(path)
        with open(path,'wb') as f:
            for data in file_obj:
                f.write(data)      
    return JsonResponse(3,safe=False)