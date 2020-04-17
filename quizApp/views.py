from django.shortcuts import get_object_or_404, render, redirect
from django.http import Http404

from .models import Quiz, Question
from django.contrib.auth.decorators import login_required, user_passes_test
from django.contrib.auth.models import Group, User



def user_is_admin(user):
    return user.groups.filter(name='quiz_admin').count()


def user_is_maker(user):
    return user.groups.filter(name='quiz_maker').count()


def user_is_taker(user):
    return user.groups.filter(name='quiz_taker').count()



@login_required(login_url='/accounts/login/')
def index(request):
        g = request.user.groups.all()
        print(g)
        if user_is_admin(request.user):
            print("asdklasjdlkasjdkljaskdl")
            return redirect('quiz_admin')

        if user_is_maker(request.user):
            return redirect('quiz_maker')
        if user_is_taker(request.user):
            return redirect('quiz_taker')
        #return redirect('quiz_admin')


@login_required(login_url='/accounts/login/')
def quiz(request):
    try:
        latest_quiz_list = Quiz.objects.order_by('id')[:5]
        context = {
            'latest_quiz_list': latest_quiz_list,
        }
    except Quiz.DoesNotExist:
        raise Http404("Quiz does not exist")
    return render(request, 'quizApp/quiz.html', context)


@login_required(login_url='/accounts/login/')
def question(request, quiz):
    try:
        latest_question_list = Question.objects.filter(quiz_foreign_key=quiz)
        context = {'latest_question_list': latest_question_list}
    except Question.DoesNotExist:
        raise Http404("Question does not exist")

    return render(request, 'quizApp/question.html', context)


@login_required(login_url='/accounts/login/')
def quiz_taker(request):
    return render(request, 'quizApp/quiz_taker.html')


@login_required(login_url='/accounts/login/')
def quiz_maker(request):
    return render(request, 'quizApp/quiz_maker.html')


@login_required(login_url='/accounts/login/')
def quiz_admin(request):
    users = User.objects.all()
    context = {'users_list': users}
    return render(request, 'quizApp/quiz_admin.html', context)

