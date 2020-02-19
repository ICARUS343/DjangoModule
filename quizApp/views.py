from django.shortcuts import get_object_or_404, render
from django.http import Http404

from .models import *
from django.contrib.auth.decorators import login_required, user_passes_test


@login_required(login_url='/accounts/login/')
@user_passes_test(lambda u: u.groups.filter(name='quiz_makers').count() == 1, login_url='/quiz_taker')
def index(request):
    latest_quiz_list = Quiz.objects.order_by('id')[:5]
    context = {
        'latest_quiz_list': latest_quiz_list,
    }
    return render(request, 'quizApp/quiz.html', context)


@login_required(login_url='/accounts/login/')
@user_passes_test(lambda u: u.groups.filter(name='quiz_makers').count()  == 1, login_url='/quiz_taker')
def question(request, quiz):
    try:
        latest_question_list = Question.objects.filter(quiz_foreign_key = quiz)
        context = {'latest_question_list': latest_question_list}
    except Question.DoesNotExist:
        raise Http404("Question does not exist")

    return render(request, 'quizApp/question.html', context)

@login_required(login_url='/accounts/login/')
@user_passes_test(lambda u: u.groups.filter(name='quiz_takers').count() == 1, login_url='/quiz_admin')
def quiz_taker(request):
    return render(request, "quizApp/quiz_taker.html")

@login_required(login_url='/accounts/login/')
@user_passes_test(lambda u: u.groups.filter(name='quiz_admin').count() == 1, login_url='/quiz_taker')
def quiz_admin(request):
    return render(request, "quizApp/quiz_admin.html")


