from django.shortcuts import get_object_or_404, render
from django.http import Http404

from django.contrib.auth.forms import UserCreationForm


# Create your views here.

def login(request):
    return render(request, 'registration/register.html')


def register(request):
    form = UserCreationForm()
    context = {'form' : form}
    return render(request, 'registration/register.html', context)