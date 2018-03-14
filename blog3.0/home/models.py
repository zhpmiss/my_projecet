from django.db import models

# Create your models here.

#一个类表示代表一个表
#属性名：字段名
class article(models.Model):
    title=models.CharField(max_length=100,verbose_name='标题')
    author=models.CharField(max_length=100,verbose_name='作者')
    describe=models.CharField(max_length=300,default='描述',verbose_name='描述')
    body=models.TextField(null=True,blank=True,verbose_name='详细')
    add_time=models.DateTimeField(auto_now=True)

class admin(models.Model):
    username=models.CharField(max_length=50)
    password=models.CharField(max_length=50)

#用户表user
class user(models.Model):
    uid =models.AutoField(primary_key=True)
    name=models.CharField(max_length=30,verbose_name='姓名')
    age =models.IntegerField(verbose_name='年龄')
    birthday=models.DateTimeField(verbose_name='出生日期',null=True,blank=True)
    #email=models.EmailField(verbose_name='邮箱')
    about=models.TextField(verbose_name='介绍')
    add_time=models.DateTimeField(auto_now_add=True)



