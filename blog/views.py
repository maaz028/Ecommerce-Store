from django.db import models
from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render
from .models import post

# Create your views here.

def index(request):
    post_data = post.objects.all()
    return render(request,'blog/index.html', {'post':post_data})

def post_func(request):
    return render(request, 'blog/post.html')

def post_view(request, id):
    post_data = post.objects.filter(post_id=id)
    
    return render(request, 'blog/post_view.html',{'post_data':post_data})