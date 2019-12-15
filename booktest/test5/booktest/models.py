from django.db import models

# Create your models here.

class AreaInfo(models.Model):
    '''地区模型类'''
    atitle=models.CharField(verbose_name='标题',max_length=20)
    #自关联属性
    aParent=models.ForeignKey('self',null=True,blank=True)

    #显示出名字 重写
    def __str__(self):
        return self.atitle

    def title(self):
        return self.atitle
    #指定方法对应的类根据哪个字段进行排序
    title.admin_order_field='atitle'
    title.short_description='地区名称'

    #返回父级地区标题
    def parent(self):
        if self.aParent is None:
            return ''
        return self.aParent.atitle
    parent.short_description = '父级地区'

class PicTest(models.Model):
    '''上传图片'''
    goods_pic=models.ImageField(upload_to='booktest')


















