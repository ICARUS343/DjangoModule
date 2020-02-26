from django import forms

user_group1 = (
        ("quiz_admins", "quiz_admins"),
        ("quiz_makers", "quiz_makers"),
        ("quiz_takers", "quiz_takers"),
    )
<<<<<<< HEAD
    user_group = forms.MultipleChoiceField(choices=user_group1, widget=forms.CheckboxSelectMultiple)

    class Meta:
        model = User
        fields = ('username', 'user_group', 'password1', 'password2',)
=======


class RegisterForm(forms.Form):
    username = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}))
    password1 = forms.CharField(widget=forms.PasswordInput(attrs={'class':'form-control'}))
    password2 = forms.CharField(widget=forms.PasswordInput(attrs={'class':'form-control'}))
    user_group = forms.ChoiceField(label ='', choices = user_group1, widget=forms.Select(attrs={'class':'form-control'}))
>>>>>>> 78396728bf2e735de201865a0c9f8c355e162a4e
