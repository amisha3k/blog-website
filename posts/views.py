from django.shortcuts import render
from .models import Post
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required

# Create your views here.
def posts_list(request):
    posts = Post.objects.all().order_by('-date')
    return render(request, 'posts/posts_list.html', {'posts':posts})

def post_page(request,slug):
    post = Post.objects.get(slug=slug)
    return render(request, 'posts/post_page.html', {'post':post})

@login_required(login_url="/users/login/")   #check if user is locked in , if not then it will redirect to login page
def post_new(request):
    return render(request,'posts/post_new.html')

    

