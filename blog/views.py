from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponseRedirect,HttpResponse
from django.utils import timezone
from .models import Blog

def delete(request):

    item=get_object_or_404(Blog,pk=request.GET.get('id)'))
    item.delete()
    return HttpResponseRedirect('')

def detail(request, blog_id):
    blog_detail = get_object_or_404(Blog, pk=blog_id)
    return render(request, 'blog/detail.html', {'blog' : blog_detail})

def create(request):
    blog = Blog()
    blog.title = request.GET['title']
    blog.body = request.GET['body']
    blog.pub_date = timezone.datetime.now()
    blog.save()
    return redirect('/blog/'+str(blog.id))

def new(request):
    return render(request, 'blog/new.html')

def home(request):
    blogs = Blog.objects
    return render(request, 'blog/home.html', { 'blogs' : blogs})
# Create your views here.
