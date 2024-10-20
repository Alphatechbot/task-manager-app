from django import forms
from django.utils import timezone
from .models import TodoList
from django.contrib.auth.forms import UserCreationForm
from users.models import MyUser


class MyUserCreationForm(UserCreationForm):
    class Meta:
        model = MyUser
        fields = [
           'username', 'email', 'password1', 'password2'
        ]


class UpdateForm(forms.ModelForm):
    name = forms.CharField(max_length=300)

    class Meta:
        model = TodoList
        fields = {
            'name',
        }
