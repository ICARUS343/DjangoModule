from django.shortcuts import get_object_or_404, render

from .models import *


def index(request):
    latest_quiz_list = Quiz.objects.order_by('id')[:5]
    context = {
        'latest_quiz_list': latest_quiz_list,
    }
    return render(request, 'quizApp/quiz.html', context)


def question(request, quiz_id):
    try:
        latest_question_list = Question.objects.filter(pk=quiz_id)
        context = {'latest_question_list': latest_question_list,}
    except Question.DoesNotExist:
    raise Http404("Question does not exist")


    return render(request, 'quizApp/question.html', context)


def question(request):
    latest_question_list = Question.objects.filter(quiz_foreign_key=(request.session['my_key']))
    context = {
        'latest_question_list': latest_question_list,
    }
    return render(request, 'quizApp/question.html', context)
