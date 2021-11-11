from django import forms
from django.core import validators
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm


class UserCreateForm(UserCreationForm):
    username = forms.CharField(validators=[validators.MaxLengthValidator(5)])
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']