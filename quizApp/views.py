from django.shortcuts import render

from django.template import loader
from .models import Quiz

def index(request):
    latest_quiz_list = Quiz.objects.order_by('id')[:1]
    template = loader.get_template('quizApp/index.html')
    context = {
	'latest_quiz_list' : latest_quiz_list,
    }
    return render(request, 'quizApp/index.html', context)
