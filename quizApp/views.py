from django.shortcuts import render
from django.shortcuts import get_object_or_404, render

from .models import *

def index(request):
    latest_quiz_list = Quiz.objects.order_by('id')[:5]
    context = {
	'latest_quiz_list' : latest_quiz_list,
    }
    return render(request, 'quizApp/quiz.html', context)

def question(request, Quiz_id):
    latest_question_list = get_object_or_404(Quiz_id)
    context = {
        'latest_question_list': latest_question_list,
    }
    return render(request, 'quizApp/question.html', context)

