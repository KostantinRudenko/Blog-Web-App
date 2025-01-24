from django.shortcuts import render, HttpResponseRedirect
from django.contrib import auth
from django.urls import reverse

from .forms import UserAuthenticationForm

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
               "form" : UserAuthenticationForm()}
    return render(request, 'user_app/login.html', context)

def signup(request):
    context = {"title" : "Signup"}
    return render(request, 'user_app/signup.html', context)