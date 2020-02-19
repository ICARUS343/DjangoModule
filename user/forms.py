from django import forms
from django.forms import ModelForm
from django.contrib.auth.models import User


class SignUpForm(ModelForm):
    first_name = forms.CharField(max_length=30, required=False, help_text='Optional.')
    last_name = forms.CharField(max_length=30, required=False, help_text='Optional.')
    CHOICES = (
        ('1', 'quiz_admin'),
        ('2', 'quiz_maker'),
        ('3', 'quiz_taker'),
    )
    select = forms.ChoiceField(widget=forms.Select, choices=CHOICES)

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'CHOICES', 'password1', 'password2',)