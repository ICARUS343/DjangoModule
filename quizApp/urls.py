from django.urls import path

from . import views

urlpatterns = [
    path('', views.pagelogin, name='login'),
    path('question', views.question, name = 'question'),
    # ex: /quizApp/5/
    path('<quiz>/', views.index, name='quiz_detail'),
    # ex: /quizApp/5/question/
    path('<quiz>/question/', views.question, name='question'),
    # ex: /quizApp/5/answer/
    #path('<int:quiz_id>/answer/', views.answer_detail, name='answer_detail'),
]
