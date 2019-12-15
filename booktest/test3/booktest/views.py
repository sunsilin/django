from django.shortcuts import render,redirect
from django.http import HttpResponse,JsonResponse
from datetime import datetime
# Create your views here.
# request就是httpRequest类型的对象
# requesst包含浏览器请求的信息

def index(request):
    '''首页'''
    # num='a'+1
    print(request.method)
    return render(request,'booktest/index.html')


def show_arg(request,num):
    return HttpResponse(num)

def login(request):
    '''显示登陆页面'''

    #判断用户是否登陆
    if request.session.has_key('islogin'):
        #用户已经登录 跳转到首页
        return redirect('/index')
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
    print(request.method)

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
        #用户密码正确 跳转到首页
        response =redirect('/index')
        # 记住用户的登录状态
        # 只要session中有islogin，就认为用户已经登陆
        request.session['islogin'] = True
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

    # 3返回应答
def logout(request):
    request.session.flush()
    return redirect('/login')

#test_ajax
def ajax_test(request):
    '''显示ajax页面'''
    return render(request,'booktest/test_ajax.html')

def ajax_handle(request):
    '''ajax请求处理'''
    return JsonResponse({'res':1})

#/login_ajax
def login_ajax(request):
    '''显示ajax页面'''
    return render(request,'booktest/login_ajax.html')
#/login_ajax_check
def login_ajax_check(request):
    '''ajax登陆校验'''
    username=request.POST.get('username')
    password=request.POST.get('password')
    print(username,password)
    if username=='smart' and password=='123':
         return  JsonResponse({'res':1})
    else:
        return JsonResponse({'res':0})
#/set cookie
def set_cookie(request):
    '''设置cookie信息 '''
    response=HttpResponse('设置cookie')
    #设置一个cookie信息  名字为num  值为1
    response.set_cookie('num',1,max_age=14*24*3600)#秒数
    # response.set_cookie('num',1,expires=datetime.now()+timedelta(days=14))



    #返回response
    return response



def get_cookie(request):
    '''获取cookie的信息'''
    #取出cookie num 的值
    num=request.COOKIES['num']
    return HttpResponse(num)


#/set_session
def set_session(request):
    '''设置session'''
    request.session['username']='smart'
    request.session['age']=18
    # request.session.set_expiry(5)#设置过期时间

    return HttpResponse('设置session')

#/get session
def get_session(request):
    '''获取session'''
    username=request.session['username']
    age=request.session['age']
    return HttpResponse(username+':'+str(age))

#/claer_session
def clear_session(request):
    '''清除session信息'''
    # request.session.clear()
    request.session.flush()
    return HttpResponse('ok')



























