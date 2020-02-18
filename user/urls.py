from django.urls import path

from . import views

urlpatterns = [
    path('', views.login, name='index'),
    path('accounts/login', views.login, name='login'),


    

]
