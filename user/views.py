from django.shortcuts import render
from django.shortcuts import get_object_or_404, render
from django.http import Http404

# Create your views here.
def index(request):
    return render(request, 'registration/login.html')
