from django.conf.urls import url
from booktest import views

urlpatterns=[
    url(r'^index$',views.index),#建立/index和视图的关系
    # 通过url函数设置url配置
    url(r'^books$',views.show_books),#显示图书信息
    url(r'^books/(\d+)$',views.detail),#显示英雄信息
]