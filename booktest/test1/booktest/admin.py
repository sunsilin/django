#coding=utf-8
from django.contrib import admin
from booktest.models import BookInfo,HeroInfo

# 后台管理相关文件


# Register your models here.

# 自定义模型管理类

class BookInfoAdmin(admin.ModelAdmin):
    list_display = ['id','btitle','bpub_date',]

class HeroInfoAdmin(admin.ModelAdmin):
    list_display = ['id','hname','hcomment',]


admin.site.register(BookInfo,BookInfoAdmin)
admin.site.register(HeroInfo,HeroInfoAdmin)

