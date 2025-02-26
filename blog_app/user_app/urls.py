from django.urls import path

from user_app.views import UserLoginView, SignupView, EmailVerificationView, profile

app_name = 'user'

urlpatterns = [
    path('login/', UserLoginView.as_view(), name='login'),
    path('signup/', SignupView.as_view(), name='signup'),
    path('verify/<str:email>/<uuid:uuid>', EmailVerificationView.as_view(), name="verification"),
    path('profile/', profile, name='profile'),
]
