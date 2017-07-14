from django.shortcuts import render,get_object_or_404
from .models import Post,Tag,Category
import markdown
from comments.forms import CommentForm
from django.db.models.aggregates import Count
from markdown.extensions.toc import TocExtension
from django.utils.text import slugify
from django.core.paginator import Paginator,EmptyPage,PageNotAnInteger
# Create your views here.
def index(request):
    post_list = Post.objects.all().order_by('-created_time')
    paginator = Paginator(post_list,2)
    page = request.GET.get('page')
    try:
        post_list = paginator.page(page)
    except PageNotAnInteger:
        post_list = paginator.page(1)
    except EmptyPage:
        post_list = paginator.page(paginator.num_pages)
    return render(request, 'index.html', context={'post_list':post_list})

def detail(request,pk):
    post = get_object_or_404(Post,pk=pk)
    md = markdown.Markdown(extensions=[
        'markdown.extensions.extra',
        'markdown.extensions.codehilite',
        TocExtension(slugify=slugify),

    ])
    post.body = md.convert(post.body)
    # post.body = markdown.markdown(post.body,extensions=[
    #     'markdown.extensions.extra',
    #     'markdown.extensions.codehilite',
    #     'markdown.extensions.toc',
    # ])
    form = CommentForm()
    comment_list = post.comment_set.all()
    context = {'post': post,
               'form': form,
               'comment_list': comment_list,
               'toc':md.toc,
               }
    return render(request,'detail.html',context=context)

def archives(request,year,month):
    post_list = Post.objects.filter(created_time__year=year,
                                    created_time__month=month,
                                    ).order_by('-created_time')
    return render(request,'index.html',context={'post_list':post_list})

def category(request, pk):
    # 记得在开始部分导入 Category 类
    cate = get_object_or_404(Category, pk=pk)
    post_list = Post.objects.filter(category=cate).order_by('-created_time')
    return render(request, 'index.html', context={'post_list': post_list})

def search(request):
    q = request.GET.get('q')
    error_msg = ''
    if not q:
        error_msg = '请输入关键词'
        return render(request,'index.html',{'error_msg':error_msg})
    post_list = Post.objects.filter(title__icontains=q)
    return render(request,'index.html',{'error_msg':error_msg,
                                        'post_list':post_list})
