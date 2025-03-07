from django.shortcuts import render, HttpResponseRedirect
from django.contrib import auth
from django.urls import reverse, reverse_lazy

from django.views.generic.edit import CreateView
from django.contrib.auth.views import LoginView
from django.contrib.messages.views import SuccessMessageMixin

from .forms import UserAuthenticationForm, UserSignupForm, UserProfileForm, PostForm

from common.views import TitleMixin

# Create your views here.

class UserLoginView(TitleMixin, LoginView):
    template_name = "user_app/login.html"
    form_class = UserAuthenticationForm
    title = "Login"

class SignupView(TitleMixin, SuccessMessageMixin, CreateView):
    template_name = "user_app/signup.html"
    form_class = UserSignupForm
    success_url = reverse_lazy("user:login")
    success_message = "You are successfully signed up"
    title = "Signup"

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