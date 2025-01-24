from django import forms

from django.contrib.auth.models import User
from django.contrib.auth.forms import AuthenticationForm

class UserAuthenticationForm(AuthenticationForm):
    username = forms.CharField(widget=forms.TextInput(attrs={'id':'username',
                                                             'placeholder':'Enter username'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'id':'password',
                                                                 'placeholder':'Enter password'}))
    class Meta:
        model = User
        fields = ['username', 'password']