from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class SignUpForm(UserCreationForm):
    user_group1 = (
        ("quiz_admins", "quiz_admins"),
        ("quiz_makers", "quiz_makers"),
        ("quiz_takers", "quiz_takers"),
    )
    user_group = forms.ChoiceField(choices=user_group1)

    class Meta:
        model = User
        fields = ('username', 'password1', 'password2','user_group',)
