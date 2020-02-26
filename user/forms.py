from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class SignUpForm(UserCreationForm):
    user_group1 = (
        ("quiz_admins", "quiz_admins (View and Remove current users.)"),
        ("quiz_makers", "quiz_makers (View and modify quiz and questions.)"),
        ("quiz_takers", "quiz_takers (Take a quiz)"),
    )
    user_group = forms.MultipleChoiceField(choices=user_group1, widget=forms.CheckboxSelectMultiple)
    class Meta:
        model = User
        fields = ('username', 'user_group', 'password1', 'password2',)
