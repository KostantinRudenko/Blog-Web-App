from django.shortcuts import render

# Create your views here.
def login(request):
    context = {"title" : "Login"}
    return render(request, 'user_app/login.html', context)

def signup(request):
    context = {"title" : "Signup"}
    return render(request, 'user_app/signup.html', context)