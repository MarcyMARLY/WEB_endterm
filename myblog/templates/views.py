from django.shortcuts import get_object_or_404,render
from django.http import HttpResponse,HttpResponseRedirect,JsonResponse, QueryDict
from django.template import loader
from django.http import Http404
from .models import Blog
from django.urls import reverse
from django.views.decorators.csrf import csrf_exempt

# Create your views here.
def index(request):
    blog_list = Blog.objects.all
    return render(request, 'blog/index.html',{'blog_list':blog_list})
def blogFunc(request):
    return render(request,'blog/blog.html',{'blog_list':Blog.objects.all})

def newblog(request):
    title = request.POST['title']
    body = request.POST['body']
    created_at = request.POST['created_at']
    b = Blog.objects.create(title = title, body = body, created_at = created_at)
    return HttpResponseRedirect(reverse('templates:index'))
def updateblog(request, id):
    title = Blog.objects.get(pk = id).title
    body = Blog.objects.get(pk=id).body
    created_at = Blog.objects.get(pk=id).created_at

    return render(request, 'blog/edit.html',{'title':title,'body':body,'created_at':created_at,'id':id,'blog_list':Blog.objects.all})
def save(request, id):
    title = request.POST['title']
    body = request.POST['body']
    created_at = request.POST['created_at']
    Blog.objects.filter(pk=id).update(title=title, body=body, created_at = created_at)
    return HttpResponseRedirect(reverse('templates:index'))
def delete(request, id):
    Blog.objects.filter(pk=id).delete()
    return HttpResponseRedirect(reverse('templates:index'))
