from django.contrib import admin
#引入模型文件
from .models import article,user
# Register your models here.
class userAdmin(admin.ModelAdmin):
    list_display = ('name','age','birthday')
    search_fields = ('name',)
    list_filter = ('name',)

class articleAdmin(admin.ModelAdmin):
    list_display = ('title','author','add_time')
    search_fields = ('title','author')
    list_filter = ('title','author')
#将表article模型注册到后台
admin.site.register(article,articleAdmin)
#将表user模型注册到后台,设置展示的方式
admin.site.register(user,userAdmin)