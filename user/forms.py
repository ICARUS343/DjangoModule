from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class SignUpForm(UserCreationForm):
    user_group1 = (
        ("quiz_admin", "quiz_admin"),
        ("quiz_maker", "quiz_maker"),
        ("quiz_taker", "quiz_taker"),
    )
    user_group = forms.ChoiceField(choices=user_group1)

    class Meta:
        model = User
        fields = ('username', 'user_group', 'password1', 'password2',)