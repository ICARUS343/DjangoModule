from django.shortcuts import render

from .models import *

def index(request):
    latest_quiz_list = Quiz.objects.order_by('id')[:5]
    context = {
	'latest_quiz_list' : latest_quiz_list,
    }
    return render(request, 'quizApp/index.html', context)

def question(request):
    latest_question_list = Question.objects.get(Quiz = Quiz)
    context = {
        'latest_quiz_list': latest_question_list,
    }
    return render(request, 'quizApp/index.html', context)

