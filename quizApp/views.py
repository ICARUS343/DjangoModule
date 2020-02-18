from django.shortcuts import get_object_or_404, render
from django.http import Http404

from .models import *
from django.contrib.auth.decorators import login_required


def pagelogin(request):
    uservalue = ''
    passwordvalue = ''

    valuenext = request.POST.get('next')

    form = Loginform(request.POST or None)
    if form.is_valid():
        uservalue = form.cleaned_data.get("username")
        passwordvalue = form.cleaned_data.get("password")

        user = authenticate(username=uservalue, password=passwordvalue)
        if user is not None and valuenext == '':
            login(request, user)

            context = {'form': form,
                       'valuenext': valuenext}

            messages.success(request, "You have successfully logged in")

            return render(request, 'accounts/Login.html', context)

        if user is not None and valuenext != '':
            login(request, user)

            messages.success(request, "You have successfully logged in")

            context = {'form': form,
                       'valuenext': valuenext}

            return redirect(valuenext)
        else:
            context = {'form': form,
                       'error': 'The username and password combination is incorrect'}

            return render(request, 'accounts/Login.html', context)

    else:

        context = {'form': form}
        return render(request, 'registration/Login.html', context)


def index(request):
        latest_quiz_list = Quiz.objects.order_by('id')[:5]
        context = {
            'latest_quiz_list': latest_quiz_list,
        }
        return render(request, 'quizApp/quiz.html', context)


def question(request, quiz):
        try:
            latest_question_list = Question.objects.filter(quiz_foreign_key = quiz)
            context = {'latest_question_list': latest_question_list}
        except Question.DoesNotExist:
            raise Http404("Question does not exist")

        return render(request, 'quizApp/question.html', context)




def auth(request):
    return render(request, '')

