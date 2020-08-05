from django.shortcuts import render,HttpResponse

# Create your views here.


# app02的首页   /app02/
def app02_base(request):
    return render(request,'app02_base.html')

