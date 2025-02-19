from django.contrib import admin
from django.urls import path, include

from post_app.views import IndexView, AboutView, contacts

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', IndexView.as_view(), name="index"),
    path('about', AboutView.as_view(), name="about"),
    path('contacts', contacts, name="contacts"),
    path('user/', include('user_app.urls', namespace="user")),
    path('posts/', include('post_app.urls', namespace="posts")),
]
