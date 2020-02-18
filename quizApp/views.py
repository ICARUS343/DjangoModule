from django.shortcuts import get_object_or_404, render
from django.http import Http404

from .models import *
from django.contrib.auth.decorators import login_required, user_passes_test


@login_required(login_url='/accounts/login/')
@user_passes_test(lambda u: u.groups.filter(name='quiz_makers').count() == 0, login_url='/access')
def index(request):
    latest_quiz_list = Quiz.objects.order_by('id')[:5]
    context = {
        'latest_quiz_list': latest_quiz_list,
    }
    return render(request, 'quizApp/quiz.html', context)


@login_required(login_url='/accounts/login/')
@user_passes_test(lambda u: u.groups.filter(name='quiz_makers').count()  == 0, login_url='/access')
def question(request, quiz):
    try:
        latest_question_list = Question.objects.filter(quiz_foreign_key = quiz)
        context = {'latest_question_list': latest_question_list}
    except Question.DoesNotExist:
        raise Http404("Question does not exist")

    return render(request, 'quizApp/question.html', context)
