

from django.conf.urls import url
from django.contrib import admin
from app01 import views,urls
# from app02 import views,urls



  # settings里面设置'DIRS': [os.path.join(BASE_DIR,'templates')],
  #  将文件夹名字templates 加入这里可以直接引用文件名
urlpatterns = [
    # app01的首页
    url(r'^$',views.app01_base)



]
