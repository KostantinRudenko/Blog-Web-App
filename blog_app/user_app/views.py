from django.shortcuts import render, HttpResponseRedirect
from django.contrib import auth
from django.urls import reverse, reverse_lazy

from django.views.generic.base import TemplateView
from django.views.generic.edit import CreateView
from django.contrib.auth.views import LoginView
from django.contrib.messages.views import SuccessMessageMixin

from .forms import UserAuthenticationForm, UserSignupForm, UserProfileForm, PostForm
from .models import BaseUser, EmailVerification

from common.views import TitleMixin

# Create your views here.

class UserLoginView(TitleMixin, LoginView):
    template_name = "user_app/login.html"
    form_class = UserAuthenticationForm
    title = "Login"

class SignupView(TitleMixin, SuccessMessageMixin, CreateView):
    template_name = "user_app/signup.html"
    form_class = UserSignupForm
    model = BaseUser
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

class EmailVerificationView(TitleMixin, TemplateView):
    title = "Email Verification"
    template_name = "user_app/email_verification.html"
    
    def get(self, request, *args, **kwargs):
        code = kwargs["uuid"]
        user = BaseUser.objects.get(email=kwargs["email"])
        verifivation = EmailVerification.objects.filter(user=user, code=code)
        if verifivation.exists() and not verifivation.first().is_expired():
            user.is_verified = True
            user.save()
            return super(EmailVerificationView, self).get(request, *args, **kwargs)
        else:
            return HttpResponseRedirect(reverse("index"))