from django.urls import path
from django.shortcuts import render

from . import views

urlpatterns = [
    path('', views.index, name='quiz'),
    path('<int:quiz_id>', views.index, name = 'quiz'),
    # ex: /quizApp/5/
    path('<int:quiz_id>/question', views.question, name='question'),
    # ex: /quizApp/5/question/
    #path('<int:quiz_id>/question/', views.question, name='question'),
    # ex: /quizApp/5/answer/
    #path('<int:quiz_id>/answer/', views.answer_detail, name='answer_detail'),
]
