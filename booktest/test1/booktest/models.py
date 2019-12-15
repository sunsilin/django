#coding=utf-8
from django.db import models
# Create your models here.
# 图书类
class BookInfo(models.Model):
    # 图书名称，CharField说明是一个字符串类型 max_length说明字段长度
    btitle=models.CharField(max_length=30)
    # 图书出版日期，DateField说明是一个日期类型
    bpub_date=models.DateField()


    def __str__(self):
        return self.btitle



# 英雄人物类
class HeroInfo(models.Model):
    hname=models.CharField(max_length=30)
    hgender=models.BooleanField(default=False)
    hcomment=models.CharField(max_length=128)
    hbook=models.ForeignKey('BookInfo')
    def __str__(self):
        return self.hname