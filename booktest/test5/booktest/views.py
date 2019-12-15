from django.shortcuts import render
from django.conf import settings
from django.http import HttpResponse,JsonResponse
from booktest.models import AreaInfo
from booktest.models import PicTest
# Create your views here.

#装饰器

EXCLUDE_IPS=['172.16.179.152']
def blocked_ips(view_func):
    def wrapper(request,*view_args,**view_kwargs):
        # 获取浏览器的ip地址
        user_ip = request.META['REMOTE_ADDR']
        if user_ip in EXCLUDE_IPS:
            return HttpResponse('<h1>Forbidden</h1>')
        else:
            return  view_func(request,*view_args,**view_kwargs)

    return wrapper










#static_test
# @blocked_ips
def static_test(request):
    '''静态文件'''
    print(settings.STATICFILES_FINDERS)
    #查找静态文件的过程  先去配置的静态文件的物理目录下，找不到在去应用下的static目录下找
    # ('django.contrib.staticfiles.finders.FileSystemFinder',
    #  'django.contrib.staticfiles.finders.AppDirectoriesFinder')

    return render(request,'booktest/static_test.html')

#/index

# @blocked_ips
def index(request):
    '''首页'''
    print('----index----')
    # num='a'+1
    return render(request,'booktest/index.html')

#/show_area
from django.core.paginator import Paginator
#前端访问时  需要传递页码
def show_area(request,pindex):
    '''分页'''
    # 1：查询出所有的省级地区的信息
    areas=AreaInfo.objects.filter(aParent__isnull=True)
    # 2:分页：每页显示10条

    paginator=Paginator(areas,10)
    print(paginator.num_pages)
    print(Paginator.page_range)

    # 3:获取pindex的内容
    if pindex=='':
        pindex=1
    else:
        pindex=int(pindex)
    # page是Page类的实例对象
    page=paginator.page(pindex)

    # 2：使用模板

    return render(request,'booktest/show_area.html',
                  {'page':page})

#/show_upload
def show_upload(request):
    '''显示上传图片页面'''
    return render(request, 'booktest/upload_pic.html')



def upload_handle(request):
    '''上传图片处理'''
    # 1：获取上传文件的处理对象
    pic=request.FILES['pic']
    print(pic.name)#获取上传文件的名字
    pic.chunks()#读取文件内容


    # 2： 创建一个文件
    sava_path='%s/booktest/%s' %(settings.MEDIA_ROOT,pic.name)
    with open(sava_path,"wb")as f:

    # 3：获取 撒谎嗯传文件的内容并写到创建的文件中
        for content in pic.chunks():
            f.write(content)
    # 4：在数据库中保存上传记录
    PicTest.objects.create(goods_pic='booktest/%s'%pic.name)
    # 5：返回应答
    return HttpResponse('ok')


# /areas
def areas(request):
    '''省市县案例'''
    return render(request,'booktest/arers.html')
# /prov
def prov(request):
    '''获取所有省级地区的信息'''
    # 1：查询出所有的省级地区的信息
    areas = AreaInfo.objects.filter(aParent__isnull=True)
    # 遍历areas并拼接出json数据：atitle id
    areas_list=[]
    for area in areas:
        areas_list.append((area.id,area.atitle))
    # 2：返回数据
    return JsonResponse({'data':areas_list})

def city(request,pid):
    '''获取pid的下级地区的信息'''
    # 获取pid对应地区的下级地区

    areas=AreaInfo.objects.filter(aParent_id=pid)
    # 遍历areas并拼接出json数据：atitle id
    areas_list = []
    for area in areas:
        areas_list.append((area.id, area.atitle))
    # 2：返回数据
    return JsonResponse({'data': areas_list})







































