from django.shortcuts import get_object_or_404,render
from django.http import HttpResponse,HttpResponseRedirect, JsonResponse
from rest_framework.parsers import JSONParser
from django.views.decorators.csrf import csrf_exempt
from django.template import loader
from django.http import Http404
from .models import Blog
from django.urls import reverse



@csrf_exempt
def blog_list(request):
    if request.method == "GET":
        blog_list = Blog.objects.all()
        blog_list_json = [b.to_json() for b in blog_list]
        return JsonResponse(blog_list_json, safe=False)

    elif request.method == "POST":
        data = request.POST
        blog = Blog()
        blog.title = data.get('title','')
        blog.body = data.get('body','')
        blog.created_at = data.get('created_at','')
        blog.save()
        return JsonResponse(blog.to_json(), status = 201)

@csrf_exempt
def blog_detail(request,id):
    try:
        blog = Blog.objects.get(pk=id)
    except Exception as e:
        return JsonResponse({"error": str(e)}, status=404)

    if request.method == "GET":
        return JsonResponse(blog.to_json())
    elif request.method == "PUT":
        data = QueryDict(request.body)
        blog.title = data.get('title', blog.title)
        blog.body = data.get('body', blog.body)
        blog.created_at = data.get('created_at', blog.created_at)
        blog.save()
        return JsonResponse(blog.to_json())
    elif request.method == "DELETE":
        blog.delete()
        return JsonResponse(blog.to_json())
