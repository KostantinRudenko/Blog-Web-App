from django.urls import path

from user_app.views import login, SignupView, profile

app_name = 'user'

urlpatterns = [
    path('login/', login, name='login'),
    path('signup/', SignupView.as_view(), name='signup'),
    path('profile/', profile, name='profile'),
]
