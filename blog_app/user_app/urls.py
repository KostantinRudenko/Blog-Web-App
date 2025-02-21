from django.urls import path

from user_app.views import UserLoginView, SignupView, profile

app_name = 'user'

urlpatterns = [
    path('login/', UserLoginView.as_view(), name='login'),
    path('signup/', SignupView.as_view(), name='signup'),
    path('profile/', profile, name='profile'),
]
