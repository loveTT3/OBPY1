"""mysite1 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
# include 用于url分发
from django.conf.urls import url,include
from django.contrib import admin
from app01 import views as app01_views ,urls as app01_urls
from app02 import views as app02_biews, urls as app02_urls

  # settings里面设置'DIRS': [os.path.join(BASE_DIR,'templates')],
  #  将文件夹名字templates 加入这里可以直接引用文件名
urlpatterns = [
    # url(r'^admin/', admin.site.urls),
    # 登陆
    url(r'^login/', app01_views.login),  
    # 有名分组
    url(r'^books/(?P<year>[0-9]{4})/$', app01_views.year_books),  # 某年的
    # 无名分组
    # url(r'^books/([0-9]{4})/$', views.year_books),  # 某年的
    url(r'^books/(?P<year>[0-9]{4})/(?P<month>[0-9]{2})/$', app01_views.year_month_books), # 某年某月的
    # url(r'^$',app01_views.base),

    # 路由分发到app01和app02的urls文件中
    url(r'^app01/',include('app01.urls')),
    url(r'^app02/',include('app02.urls')),

    # 重定向后到首页
    url(r'^base/',app01_views.base),
    url(r'^base1/',app01_views.base1.as_view()),

]
