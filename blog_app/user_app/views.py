from django.shortcuts import render

# Create your views here.
def login(request):
    return render(request, 'user_app/login.html')

def signup(request):
    return render(request, 'user_app/signup.html')