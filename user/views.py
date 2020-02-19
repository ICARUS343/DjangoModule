from django.shortcuts import get_object_or_404, render, redirect
from django.contrib.auth.models import Group

from django.contrib.auth import logout as auth_logout

from .forms import SignUpForm
from django.contrib.auth import authenticate, login as auth_login


def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        if user is not None:
            if user.is_active:
                auth_login(request, user)
                return redirect('/quizApp/')
            else:
                return redirect('/accounts/register/')
    return render(request, 'registration/login.html')


def register(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            user = authenticate(username=username, password=password)
            group = Group.objects.get(name=user.cleaned_data['user_group'])
            user.groups.add(group)
            auth_login(request, user)
            return redirect('/quizApp/')
    else:
        form = SignUpForm(request.POST)
    context = {'form' : form}
    return render(request, 'registration/register.html', context)


def logout(request):
    auth_logout(request)
    return render(request, "registration/logout.html")


def access_denied(request):
    return render(request, "registration/no_access.html")