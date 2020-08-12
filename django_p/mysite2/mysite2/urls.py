from django.conf.urls import url
from django.contrib import admin
from app1 import views

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^login/', views.login),
    url(r'^tags/', views.tags),
    url(r'^muban/', views.muban),
    url(r'^jicheng1/', views.jicheng1),
    url(r'^jicheng2/', views.jicheng2),
    url(r'^jicheng3/', views.jicheng3),
    url(r'^test/', views.test),
    url(r'^zujian/', views.zujian),

]