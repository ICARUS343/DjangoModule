from django.urls import path
from django.shortcuts import render

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('quiz', views.index, name = 'quiz'),
    # ex: /quizApp/5/
    path('quiz/<int:quiz_id>/', views.question, name='question'),
    # ex: /quizApp/5/question/
    #path('<int:quiz_id>/question/', views.question, name='question'),
    # ex: /quizApp/5/answer/
    #path('<int:quiz_id>/answer/', views.answer_detail, name='answer_detail'),
]
