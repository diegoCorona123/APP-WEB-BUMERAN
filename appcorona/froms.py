from dataclasses import field, fields
from logging import PlaceHolder
from django import forms
from .models import Comentarios
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm

class ComentariosForm(forms.ModelForm):
    class Meta:
        model = Comentarios
        fields = ["nombre", "email","comentario"]
        #fields = '_all_'

class userForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'username', 'email', 'password1', 'password2']

class loginForm(AuthenticationForm):
    class Meta:
        model = User 
        fields = ['username', 'password', 'remember_me']
    username = forms.CharField(max_length=100, required=True, widget=forms.TextInput (attrs={'placeholder': 'Username', 'class': 'btn',}))
    password = forms.CharField(max_length=50, required=True, widget=forms.PasswordInput(attrs={'placeholder': 'Password', 'class': 'btn', 'data-toggle': 'password', 'id': 'password', 'name': 'password', }))
    remember_me = forms.BooleanField(required=False)