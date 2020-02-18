from django.shortcuts import get_object_or_404, render
from django.http import Http404

from .models import *
from django.contrib.auth.decorators import login_required


def index(request):
    if not request.user.is_authenticated:
        return redirect('%s?next=%s' % (settings.LOGIN_URL, request.path))
    latest_quiz_list = Quiz.objects.order_by('id')[:5]
    context = {
        'latest_quiz_list': latest_quiz_list,
    }
    return render(request, 'quizApp/quiz.html', context)


def question(request, quiz):
    if not request.user.is_authenticated:
        return redirect('%s?next=%s' % (settings.LOGIN_URL, request.path))
    try:
        latest_question_list = Question.objects.filter(quiz_foreign_key = quiz)
        context = {'latest_question_list': latest_question_list}
    except Question.DoesNotExist:
        raise Http404("Question does not exist")

    return render(request, 'quizApp/question.html', context)

def auth(request):
    return render(request, '')

