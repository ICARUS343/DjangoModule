from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    
    path('question/', views.question, name = 'question'),
    # ex: /quizApp/5/
    path('<quiz>/', views.index, name='quiz_detail'),
    # ex: /quizApp/5/question/
    path('<quiz>/question/', views.question, name='question'),
    # ex: /quizApp/5/answer/
    #path('<int:quiz_id>/answer/', views.answer_detail, name='answer_detail'),

    path('/quiz_taker/', views.quiz_taker, name='quiz_taker'),
    path('/quiz_admin/', views.quiz_admin, name='quiz_admin')

]
