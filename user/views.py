from django.shortcuts import get_object_or_404, render, redirect
from django.http import Http404

from django.contrib.auth.forms import UserCreationForm

from django.contrib.auth import authenticate, login as auth_login

# Create your views here.

def login(request):
    return render(request, 'registration/login.html')


def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)

        if form.is_valid():
            form.save()
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            user = authenticate(username = username, password = password)
            auth_login(request, user)
            return redirect('quizApp/')
    else:
        form = UserCreationForm()
    context = {'form' : form}
    return render(request, 'registration/register.html', context)