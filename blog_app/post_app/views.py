from django.shortcuts import render, HttpResponseRedirect

from .models import Post, Comments
from .forms import CreateCommentForm
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

def post(request, title):
    post = Post.objects.get(title=title)
    form = CreateCommentForm()
    if request.method == "POST":
        form = CreateCommentForm(data=request.POST)
        if form.is_valid():
            username = request.user.username
            content = form.cleaned_data["content"]
            Comments.objects.create(user=username, post=post, content=content)
            return HttpResponseRedirect(request.META["HTTP_REFERER"])
    else:
        form = CreateCommentForm()
    
    comments = Comments.objects.filter(post=post)
    context = {"title": "Post",
               "post": post,
               "comments": comments,
               "form": form}
    return render(request, 'post.html', context)