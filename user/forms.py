from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class SignUpForm(UserCreationForm):
    user_group = (
        ("1", "quiz_admin"),
        ("2", "quiz_maker"),
        ("3", "quiz_taker"),
    )
    class Meta:
        model = User
        fields = ('username', 'user_group', 'password1', 'password2', )