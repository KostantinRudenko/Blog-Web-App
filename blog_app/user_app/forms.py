import uuid
from datetime import timedelta

from django import forms

from django.contrib.auth.models import User
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm, UserChangeForm
from post_app.models import Post
from django.forms import ModelForm

from django.utils.timezone import now

from .models import EmailVerification

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

    def save(self, commit=True):
        user = super(UserSignupForm, self).save(commit=True)
        expiration = now() + timedelta(hours=48)
        record = EmailVerification.objects.create(code=uuid.uuid4(), user=user, expiration=expiration)
        record.send_verification_email()
        return user

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
    
    class Meta:
        model = Post
        fields = ['title', 'content']