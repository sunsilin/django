#coding=utf-8
from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader,RequestContext
from booktest.models import BookInfo #导入图书模型


def my_render(request,template_path,context_dict={}):
    '使用模板文件'
    # 使用模板文件
    # 1.加载模板内容 ，模板对象
    temp = loader.get_template(template_path)
    # 2.定义模板上下文  给模板文件传递数据
    context = RequestContext(request, context_dict)
    # 3.模板渲染，产生标准的html内容
    res_html = temp.render(context)
    # 返回给浏览器
    return HttpResponse(res_html)



# Create your views here.
# 定义视图函数HttpRequest
# 进行urlp配置 建立url地址和试图的对应关系
def index(request):
    # 进行处理，和M和T进行交互
    # return HttpResponse('老铁，没毛病')
    # return my_render(request,'booktest/index.html')
    return render(request,'booktest/index.html',{'content':'hello world','list':list(range(1,10))})


def show_books(request):
    #显示图书的信息
    # 通过M查找图书表中的数据
    books=BookInfo.objects.all()
    #使用模板，
    return render(request,'booktest/show_books.html',{'books':books})


def detail(request,bid):
    #查询图书关联英雄信息
    #1.根据bid查询图书信息
    book=BookInfo.objects.get(id=bid)
    # 2.查询和book关联的英雄信息
    heros=book.heroinfo_set.all()
    # 3.使用模板
    return render(request,'booktest/detail.html',{'book':book,'heros':heros})
























