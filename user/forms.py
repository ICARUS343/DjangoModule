from django import forms

class NameForm(forms.Form):
    your_name = forms.CharField(label='Your name', max_length=100)
    user_group = forms.CharField(label = "Choose your authentication level", max_length=10)
