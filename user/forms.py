from django import forms
from forms import *
user_group1 = (
        ("quiz_admins", "quiz_admins"),
        ("quiz_makers", "quiz_makers"),
        ("quiz_takers", "quiz_takers"),
    )


class RegisterForm(forms.Form):
    username = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}))
    password1 = forms.CharField(widget=forms.PasswordInput(attrs={'class':'form-control'}))
    password2 = forms.CharField(widget=forms.PasswordInput(attrs={'class':'form-control'}))
    user_group = ChoiceField(label ='', choices = user_group1, widget=forms.Select(attrs={'class':'form-control'})