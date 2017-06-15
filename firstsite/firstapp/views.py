from django.shortcuts import render,redirect

# Create your views here.
from django.shortcuts import render
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from firstapp.models import Article, Category,Link
from django.db.models.aggregates import Count
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate,logout,login
from django.contrib.auth.models import User

def index(request):
    queruset = request.GET.get('tag')
    if queruset:
        article_list = Article.objects.filter(category__name__contains=queruset, Status='Complete').order_by('-id')
    else:
        article_list = Article.objects.order_by('-id').filter(Status='Complete')
    page_robot = Paginator(article_list, 5)
    page_num = request.GET.get('page')
    try:
        article_list = page_robot.page(page_num)
    except EmptyPage:
        article_list = page_robot.page(page_robot.num_pages)
    except PageNotAnInteger:
        article_list = page_robot.page(1)
    category_list = Category.objects.all().annotate(
        num_articles=Count('article')).filter(num_articles__gt=0)
    links_list = Link.objects.all()
    context = dict()
    context['article_list'] = article_list
    context['category_list'] = category_list
    context['links_list'] = links_list
    return render(request, 'index.html', context)


def detail_page(request, page_num):
    context = {}
    article = Article.objects.get(id=page_num)
    context['article'] = article
    return render(request, 'detail.html', context)


def categoty(request):
    return render(request, 'index.html', {})


def about(request):
    context = {}
    return render(request, 'about.html', context)

def link(request):
    return render(request,'index.html',{})

def acc_login(request):
    errors =  {}
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        user = authenticate(username=username,password=password)
        print("auth res",user)
        if user:
            print("Authenticate success")
            login(request,user)
            return redirect("/admin")
        else:
            errors = {"error": "Wrong username or password!"}
    return render(request, "login.html", errors)

def acc_register(request):
    return render(request,'register.html')