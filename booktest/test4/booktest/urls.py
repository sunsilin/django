from django.conf.urls import  url
from booktest import views

urlpatterns = [
    url(r'^index$',views.index,name='index'),
    url(r'^index2$',views.index2),#模板文件加载顺序
    url(r'^temp_var$',views.temp_var),#模板变量
    url(r'^temp_tags$',views.temp_tags),#模板标签
    url(r'^temp_filter$', views.temp_filter),  # 模板过滤器
    url(r'^temp_inherit$',views.temp_inherit),#模板继承
    url(r'^html_escape$',views.html_escape),#html转义
    url(r'^login$',views.login),#现实登陆页面
    url(r'^login_check$',views.login_check),#登陆校验
    url(r'^change_pwd$',views.change_pwd),#显示修改密码页面

    # login_required(change_pwd)(request,*view_args,**view_kwargs)
    url(r'^change_pwd_action$',views.change_pwd_action),#修改密码处理
    url(r'^url_reverse$',views.url_reverse),#url反向解析
    url(r'^show_args/(\d+)/(\d+)$',views.show_args,name='show_args'),#url反向解析 捕获位置参数
    url(r'^show_kwargs/(?P<c>\d+)/(?P<d>\d+)$', views.show_kwagrs, name='show_kwargs'),  # url反向解析 捕获关键字参数
    url(r'^test_redirect$',views.test_redirect),#视图里面的动态解析ulr
]
