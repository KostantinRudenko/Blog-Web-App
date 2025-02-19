from django.shortcuts import render, HttpResponseRedirect
from django.contrib import auth, messages
from django.urls import reverse

from .forms import UserAuthenticationForm, UserSignupForm, UserProfileForm, PostForm

# Create your views here.
def login(request):
    if request.method == "POST":
        form = UserAuthenticationForm(data=request.POST)
        if form.is_valid():
            username = request.POST['username']
            password = request.POST['password']
            user = auth.authenticate(username=username, password=password)
            if user:
                auth.login(request, user)
                return HttpResponseRedirect(reverse('index'))
    else:
        form = UserAuthenticationForm()
    context = {"title" : "Login",
               "form" : form}
    return render(request, 'user_app/login.html', context)

def signup(request):
    if request.method == "POST":
        form = UserSignupForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Account created successfully!")
            return HttpResponseRedirect(reverse('user:login'))
    else:
        form = UserSignupForm()
    context = {"title" : "Signup",
               'form' : form}
    return render(request, 'user_app/signup.html', context)

def profile(request):
    post_form = PostForm()
    if request.method == "POST":
        if "logout" in request.POST:
            auth.logout(request)
            return HttpResponseRedirect(reverse('index'))
        
        elif "create-post" in request.POST:
            form = PostForm(data=request.POST)
            if form.is_valid():
                form.save()
                return HttpResponseRedirect(reverse('user:profile'))
            
        else:
            form = UserProfileForm(data=request.POST, instance=request.user)
            if form.is_valid():
                form.save()
                return HttpResponseRedirect(reverse('user:profile'))
    else:
        form = UserProfileForm(instance=request.user)
        post_form = PostForm()
    context = {"title" : "Profile",
               "form" : form,
               "post_form" : post_form}
    return render(request, 'user_app/profile.html', context)