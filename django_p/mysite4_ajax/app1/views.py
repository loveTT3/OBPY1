from django.shortcuts import render,HttpResponse
from django.http import JsonResponse
# Create your views here.

def login(request):
    return render(request,'login.html')


# 局部刷新  返回的不是界面 
def ajax_add(request):
    i1 = int(request.GET.get('i1'))
    i2 = int(request.GET.get('i2'))
    ret = i1+i2
    # print(ret)
    return JsonResponse(ret, safe=False)
