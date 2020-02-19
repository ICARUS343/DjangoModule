from django.shortcuts import get_object_or_404, render, redirect
from django.http import Http404

from .models import *
from django.contrib.auth.decorators import login_required, user_passes_test
from django.contrib.auth.models import Group


@login_required(login_url='/accounts/login/')
def index(request):
    users_in_admin = Group.objects.get(name="quiz_admins").user_set.all()
    users_in_taker = Group.objects.get(name="quiz_takers").user_set.all()
    users_in_maker = Group.objects.get(name="quiz_makers").user_set.all()
    if request.user in users_in_admin:
        return redirect('quiz_admin')
    if request.user in users_in_taker:
        return redirect('quiz_maker')
    if request.user in users_in_maker:
        latest_quiz_list = Quiz.objects.order_by('id')[:5]
        context = {
            'latest_quiz_list': latest_quiz_list,
        }
        return render(request, 'quizApp/quiz.html', context)
    else:
        return render(request, '/access')

@login_required(login_url='/accounts/login/')
def question(request, quiz):
    try:
        latest_question_list = Question.objects.filter(quiz_foreign_key = quiz)
        context = {'latest_question_list': latest_question_list}
    except Question.DoesNotExist:
        raise Http404("Question does not exist")

    return render(request, 'quizApp/question.html', context)


@login_required(login_url='/accounts/login/')
def quiz_taker(request):
    return render(request, "quizApp/quiz_taker.html")


@login_required(login_url='/accounts/login/')
def quiz_admin(request):
    return render(request, "quizApp/quiz_admin.html")

