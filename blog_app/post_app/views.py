from django.shortcuts import render

from .models import Post
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