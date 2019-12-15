from django.shortcuts import render,redirect#导入重定向函数
from booktest.models import BookInfo,AreaInfo
from datetime import  date
from django.http import HttpResponse,HttpResponseRedirect


# Create your views here.
def index(request):
    '''显示图书信息'''
    # 1:查询出所有的图书信息
    books=BookInfo.objects.all()
    # 使用模板
    return render(request,'booktest/index.html',{'books':books})
def create(request):
    '''新增一本图书'''
    b=BookInfo()
    b.btitle='流星蝴蝶剑'
    b.bpub_date=date(1990,1,1)
    # 2保存进数据库
    b.save()
    # 返回应答,让浏览器再访问Index,重定向
    # return HttpResponseRedirect('/index')

    return redirect('/index')

def delete(request,bid):
    '''删除点击的图书'''
    #1通过bid获取图书对象
    book=BookInfo.objects.get(id=bid)
    #2删除
    book.delete()
    # 3 重定向 让浏览器访问/index
    # return HttpResponseRedirect('/index')
    return redirect('/index')



def arears(request):
    # 获取广州市的上级地区和下级地区

    # 1:获取广州市的信息
    area=AreaInfo.objects.get(atitle='广州市')

    # 2:查询广州市的上级地区
    parent=area.aParent
    # 3:查询广州市的下级地区
    children=area.areainfo_set.all()
    #使用模板
    return render(request,"booktest/areas.html",{'area':area,'parent':parent,'children':children})




















