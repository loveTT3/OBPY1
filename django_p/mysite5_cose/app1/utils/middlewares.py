from django.shortcuts import redirect,HttpResponse,render
from django.utils.deprecation import MiddlewareMixin

class md1(MiddlewareMixin):
    def process_request(self,request):
        print('访问路径------------',request.path)
        print('这是MD1的request')
        path = request.path
        if path == '/index/' or path == '/logout/':
            return None
        else:
            coo = request.COOKIES.get('k1')
            print(coo)
            print(path)
            if coo == 'v1':
                return None
            else:
                return redirect('index')
            
    def process_response(self,request,response):
        print('这是MD1的response')
        return response


class md2(MiddlewareMixin):
    def process_request(self,request):
        print('MD2的request')
        return None
    def process_response(self,request,response):
        print('MD2的response')
        return response
