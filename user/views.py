from django.shortcuts import get_object_or_404, render, redirect
from django.contrib.auth.models import Group
from django.shortcuts import get_object_or_404
from .forms import SignUpForm

from django.contrib.auth import authenticate, login as auth_login, logout as auth_logout


def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        if user is not None:
            if user.is_active:
                auth_login(request, user)
                return redirect('quizApp/')
            else:
                return redirect('/accounts/register/')
    return render(request, 'registration/login.html')


def register(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username1 = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username1, password=raw_password)
            user_group = form.cleaned_data.get('user_group')
            for assignment in user_group:
                g = Group.objects.get(name=assignment)
                g.user_set.add(user)
                user.groups.add(g)
            auth_login(request, user)
            return redirect('quizApp/')
    else:
        form = SignUpForm()
    return render(request, 'registration/register.html', {'form': form})


def logout(request):
    auth_logout(request)
    return render(request, "registration/logout.html")


def access_denied(request):
    return render(request, "registration/no_access.html")

