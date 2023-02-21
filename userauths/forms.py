from django import forms
from django.contrib.auth.forms import UserCreationForm
from userauths.models import User


class UserRegisterForm(UserCreationForm):
    # Use this UserCreationForm to create a new user auth, access it from the admin panel
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']