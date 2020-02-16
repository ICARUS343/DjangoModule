from django.shortcuts import render


from .models import *


def index(request):
    latest_quiz_list = Quiz.objects.order_by('id')[:5]
    context = {
	'latest_quiz_list' : latest_quiz_list,
    }
    return render(request, 'quizApp/quiz.html', context)


def question(request, id):
    latest_question_list = Question.objects.filter(quiz_foreign_key = id)
    context = {
        'latest_question_list': latest_question_list,
    }
    return render(request, 'quizApp/question.html', context)





