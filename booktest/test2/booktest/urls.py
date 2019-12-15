
from django.conf.urls import url
from booktest import views


urlpatterns = [
    url(r'^index$',views.index),#图书信息页面
    url(r'^create$',views.create),#新增一本图书
    url(r'^delete(\d+)$',views.delete),
    url(r'^areas$',views.arears),#自关联案例
]
