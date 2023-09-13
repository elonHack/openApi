from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm


class CreateUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ('username', 'email', 'password')

class LoginForm(AuthenticationForm):
    username = forms.CharField(max_length= 20, required=False, widget=forms.TextInput())
    password = forms.CharField(widget=forms.PasswordInput())