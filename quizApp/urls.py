from django.urls import path

from . import views

urlpatterns = [
    path('quizApp', views.index, name='index'),
    path('', views.question, name = 'question'),
    # ex: /quizApp/5/
    #path('<int:quiz_id>/', views.quiz_detail, name='quiz_detail'),
    # ex: /quizApp/5/question/
    #path('<int:quiz_id>/question/', views.question_detail, name='question_detail'),
    # ex: /quizApp/5/answer/
    #path('<int:quiz_id>/answer/', views.answer_detail, name='answer_detail'),
]
