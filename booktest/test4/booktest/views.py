from django.shortcuts import render,redirect
from django.template import loader,RequestContext
from django.http import HttpResponse
from booktest.models import Bookinfo

# Create your views here.
#登陆装饰器
def login_required(view_func):
    '''登陆判断装饰器'''
    def wrapper(request,*view_args,**view_kwargs):
        #判断用户是否登陆
        if request.session.has_key('islogin'):
            #用户已经登陆，调用对应的视图
            return view_func(request,*view_args,**view_kwargs)
        else:
            #用户没有登陆，跳转到登陆页面
            return redirect('/login')
    return wrapper

def my_render(request,template_path,context={}):
    # 1:加载模板文件，获取一个模板对象
    temp = loader.get_template(template_path)

    # 2：定义模板上下文，给模板文件传数据
    context = RequestContext(request, context)
    # 3：模板渲染，产生一个替换后的html内容
    res_html = temp.render(context)

    # 4：返回应答
    return HttpResponse(res_html)

#/index
def index(request):
    return my_render(request,'booktest/index.html')

#/index2
def index2(request):
    '''模板文件加载顺序'''
    return render(request,'booktest/index2.html')
#temp_var
def temp_var(request):
    '''模板变量'''
    my_dict={'title':'字典键值'}
    my_list=[1,2,3]
    book=Bookinfo.objects.get(id=1)
    #定义模板上下文
    context={'my_dict':my_dict,"my_list":my_list,'book':book}

    return render(request,'booktest/temp_var.html',context)

#temp_tags
def temp_tags(request):
    '''模板标签'''
    # 1:查找所有的图书信息
    books=Bookinfo.objects.all()
    return render(request,'booktest/temp_tags.html',{'books':books})

#temp_filter
def temp_filter(request):
    '''模板过滤器'''
    # 1:查找所有的图书信息
    books=Bookinfo.objects.all()
    return render(request,'booktest/temp_filter.html',{'books':books})


#/temp_inherit
def temp_inherit(request):
    '''模板继承'''
    return render(request,'booktest/child.html')

#/html_escape
def html_escape(request):
    '''html转义'''
    return render(request,'booktest/html_escape.html',{'content':'<h1>hello</h1>'})

def login(request):
    '''显示登陆页面'''

    #判断用户是否登陆
    if request.session.has_key('islogin'):
        #用户已经登录 跳转到修改密码页面
        return redirect('/change_pwd')
    else:
        #用户未登录
        # 获取cookie username

        if 'username' in  request.COOKIES:
            # 获取记住的用户名
            username=request.COOKIES['username']
        else:
            username=''
        return render(request, 'booktest/login.html',{'username':username})


def login_check(request):
    '''登陆校验视图'''
    # request.POST保存的是post提交的参数
    # request.GET保存的是get提交的参数
    # print(request.method)

    # 1获取提交的用户名和密码
    username=request.POST.get('username')
    password=request.POST.get('password')
    remember=request.POST.get('remember')
    print(remember)


    # print('username'+':'+'password')
    # 2进行登陆的校验
    # 实际开发是 根据用户名和密码查找数据库
    # 模拟 用户名smart 密码123
    if username=='smart' and password=='123':
        #用户密码正确 跳转到修改密码页面
        response =redirect('/change_pwd')
        # 记住用户的登录状态
        # 只要session中有islogin，就认为用户已经登陆
        request.session['islogin'] = True
        #记住登陆的用户名
        request.session['username']=username
        #判断是否需要记住用户名
        if remember=='on':
            #设置cookie 的username 过期时间为1周
            response.set_cookie('username',username,max_age=7*24*3600)

            # 记住用户的登录状态
            # 只要session中有islogin，就认为用户已经登陆


        return response


    else:
        #用户或密码错误 跳转到登陆页面
        return redirect('/login')

#/change_pwd
@login_required
def change_pwd(request):
    '''显示修改密码页面'''
    #
    return render(request,'booktest/change_pwd.html')


#/change_pwd_action
@login_required
def change_pwd_action(request):
    '''模拟修改密码处理'''
    # 1：获取新密码
    pwd=request.POST.get('pwd')
    # 获取用户名
    username=request.session.get('username')
    # 2：实际开发的时候，修改对应数据库中的内容
    return HttpResponse('修改密码为%s,修改人为%s'%(pwd,username))
    #3：返回一个应答

#url_reverse
def url_reverse(request):
    '''url反向解析'''
    return render(request,'booktest/url_reverse.html')

def show_args(request,a,b):
    '''url反向解析，捕获位置参数'''
    return  HttpResponse(a+':'+b)


def show_kwagrs(request,c,d):
    '''url反向解析，捕获关键字参数'''
    return HttpResponse(c+':'+d)

from django.core.urlresolvers import reverse

# /test_redirect
def test_redirect(request):
    #重定向到index
    # url=reverse('booktest:index')

    #重定向到/show_args/1/2
    # url=reverse('booktest:show_args',args=(1,2))

    #重定向到show_kwargs/3/4
    url=reverse('booktest:show_kwargs',kwargs={'c':3,'d':4})
    return redirect(url)























