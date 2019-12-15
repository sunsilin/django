# encoding=utf8
from django.db import models
import os

# Create your models here.

class BookInfoManager(models.Manager):
    '''图书模型类'''
    # 1:改变查询的结果集
    def all(self):
        # 1调用父类的all,获取所有数据
        books= super(BookInfoManager, self).all()
        # 2：对数据进行过滤
        books=books.filter(isDelete=False)
        # 3.返回books
        return books


    # 2封装函数：操作模型类对应的数据表（增删改查）
    def create_book(self,btitle,bpub_date):
        #创建一个图书类
        model_class=self.model#获取self所在的模型类

        book=model_class()




        book=BookInfo()
        book.btitle=btitle
        book.bpub_date=bpub_date
        # 保存进数据库

        book.save()
         #返回book
        return book







class BookInfo(models.Model):
    '''图书模型类'''
    #图书标题
    btitle=models.CharField(max_length=30,db_column='title')
    # 图书名字唯一,图书索引
    # btitle=models.CharField(max_length=30,unique=True,db_index=True)
    #价格 最大位数为10 小树位数为2
    # bprice=models.DecimalField(max_digits=10,decimal_places=2)
    #出版日期
    # bpub_date=models.DateField(auto_now_add=True)#创建时间 发布新闻
    bpub_date=models.DateField()
    # bpub_date=models.DateField(auto_now=True)#更新时间 修改新闻
    #阅读量
    bread=models.IntegerField(default=0)
    #评论量
    bcomment=models.IntegerField(default=0)
    #删除标记
    isDelete=models.BooleanField(default=False)


    #自定义一个manager类对象
    # book=models.Manager()
    # 自定义一个BookInfoManger类的对象
    objects=BookInfoManager()

#
# # 对象
#
#     @classmethod
#     def create_book(cls,btitle,bpub_date):
#         # 1创建一个图书对象
#         obj=cls()
#         obj.btitle=btitle
#         obj.bpub_date=bpub_date
#         # 2保存进
#         obj.save()
#         # 3返回obj
#
#         return obj


class Meta:
    db_table='bookinfo'#制定模型类对应的表名





class HeroInfo(models.Model):
    '''英雄人物模型类'''
    #英雄名称
    hname=models.CharField(max_length=30)
    # 英雄性别
    hgender=models.BooleanField(default=False)
    # 英雄技能
    hcomment=models.CharField(max_length=300,null=True,blank=False)
    # 关系属性
    hbook=models.ForeignKey('BookInfo')
    # 删除标记
    isDelete = models.BooleanField(default=False)
'''
#新闻类型类
class NewType(models.Model):
    type=models.CharField(max_length=20)

# 新闻类
class NewInfo(models.Model):
    # 新闻标题

    title=models.CharField(max_length=128)
    # 发布日期

    pub_date=models.DateTimeField(auto_now_add=True)
    #新闻内容
    content=models.TextField()
    #关联属性  多对多关系 代表新闻所属的类型
    new_type=models.ManyToManyField('NewType')


#员工基本信息类 一对一

class EmployeeBasicInfo(models.Model):
    # 姓名
    name=models.CharField(max_length=128)
    # 性别
    gender=models.BooleanField(default=False)
    # 年龄
    age=models.IntegerField()

#员工详细信息类
class EmployeeDateInfo(models.Model):
    # 详细地址
    addr=models.CharField(max_length=128)

    # 一对一关系 用关系属性 ，代表员工基本信息

    employee_basic=models.OneToOneField('EmployeeBasicInfo')'''

class AreaInfo(models.Model):
    # 地区名称
    atitle=models.CharField(max_length=30)
    #关系属性，代表当前地区的父级地区
    aParent=models.ForeignKey('self',null=True,blank=True)















