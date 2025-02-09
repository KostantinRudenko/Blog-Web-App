from django.urls import path, include

from post_app.views import post

app_name = "post_app"

urlpatterns = [
    path('<int:id>/', post, name='posts'),
]