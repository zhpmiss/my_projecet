from django.shortcuts import render,redirect,HttpResponse
from . import models
# Create your views here.
def index(request):
    res10 =models.article.objects.all()

    res1 =models.article.objects.all().values()
   # print(res1)
    return render(request,'index.html',{'res':res10,'res1':res1})

def show(request,aid):
    res=models.article.objects.get(id=aid)
    #res =models.article.objects.filter(id=aid)
    return render(request,'show.html',{'res':res})
def mydel(request,aid):
    models.article.objects.filter(id=aid).delete()
    #res =models.article.objects.all()
    #res1 =models.article.objects.all().values()
   # print(res1)
    #return render(request,'index.html',{'res':res})
    #return HttpResponse('<script>location.href="/"</script>')
    return redirect('/')

def myedit(request,aid):
     res =models.article.objects.get(id=aid)

     return render(request,'edit.html',{'res':res})
def edit_save(request):
    #print(request.POST) #request.GET
    print(request.method)#request.method 判断提交方式。
    aid=request.POST.get('id')
    # title=request.POST.get('title')
    # author = request.POST.get('author')
    # describe = request.POST.get('describe')
    # body = request.POST.get('body')
    edit_data = {
        'title': request.POST.get('title'),
        'author': request.POST.get('author'),
        'body': request.POST.get('body')
    }
    if request.POST.get('describe'):
        edit_data['describe']=request.POST.get('describe')
        #models.article.objects.filter(id=aid).update(title=title,author=author,describe =describe,body=body)
    models.article.objects.filter(id=aid).update(**edit_data)
    return redirect('/')

def add(request):
    if request.method =='GET':
        return render(request,'add.html')
    else:
        add_data = {
            'title': request.POST.get('title'),
            'author': request.POST.get('author'),
            'describe': request.POST.get('describe'),
            'body': request.POST.get('body')
        }
        models.article.objects.create(**add_data)
        return  redirect('/')


#登陆
def login(request):
    if request.method =='POST':
        #1取得用户登陆信息
        username=request.POST.get('username')
        password = request.POST.get('password')
        #。判断用户登陆信息是否正确

        res =models.admin.objects.filter(username=username,password=password)
        #使用get方式作为条件查询时，如果查询结果为空。则报错
        #res = models.admin.objects.get(username=username, password=password)
        print(res)
        if res:
            return redirect('/')
        else:
            return redirect('/login/')
    else:
        return render(request,'login.html')
