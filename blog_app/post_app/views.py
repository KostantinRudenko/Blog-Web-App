from django.shortcuts import render

from .models import Post, Comments
# Create your views here.

def index(request):
    context = {"title": "Posts",
               "posts": Post.objects.all()}
    return render(request, 'index.html', context)

def about(request):
    context = {"title": "About me"}
    return render(request, 'about.html', context)

def contacts(request):
    context = {"title": "Contacts"}
    return render(request, 'contacts.html', context)

def post(request, post_id):
    post = Post.objects.get(id=post_id)
    comments = Comments.objects.filter(post=post)
    context = {"title": "Post",
               "post": post,
               "comments": comments}
    return render(request, 'post.html', context)