from django import forms

from django.contrib.auth.models import User
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm, UserChangeForm
from post_app.models import Post
from django.forms import ModelForm

class UserAuthenticationForm(AuthenticationForm):
    username = forms.CharField(widget=forms.TextInput(attrs={'id':'username',
                                                             'placeholder':'Enter username'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'id':'password',
                                                                 'placeholder':'Enter password'}))
    class Meta:
        model = User
        fields = ['username', 'password']

class UserSignupForm(UserCreationForm):
    username = forms.CharField(widget=forms.TextInput(attrs={'id': 'username', 'placeholder': 'Enter username'}))
    email = forms.EmailField(widget=forms.TextInput(attrs={'id': 'email', 'placeholder': 'Enter email'}))
    password1 = forms.CharField(widget=forms.PasswordInput(attrs={'id': 'password1', 'placeholder': 'Enter password'}))
    password2 = forms.CharField(widget=forms.PasswordInput(attrs={'id': 'password2', 'placeholder': 'Confirm password'}))

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

class UserProfileForm(UserChangeForm):
    username = forms.CharField(widget=forms.TextInput(attrs={'id': 'username'}))
    email = forms.EmailField(widget=forms.TextInput(attrs={'id': 'email', 'readonly': True}))
    last_login = forms.DateTimeField(widget=forms.DateTimeInput(attrs={'id': 'last_login', 'readonly': True}))

    class Meta:
        model = User
        fields = ['username', 'email', 'last_login']

class PostForm(ModelForm):
    title = forms.CharField(widget=forms.TextInput(attrs={'id': 'title', 'placeholder': 'Enter title'}))
    content = forms.CharField(widget=forms.Textarea(attrs={'id': 'content', 'placeholder': 'Enter content'}))
    created_at = forms.DateTimeField(widget=forms.DateTimeInput(attrs={'id': 'time', 'readonly': True}))

    class Meta:
        model = Post
        fields = ['title', 'content']