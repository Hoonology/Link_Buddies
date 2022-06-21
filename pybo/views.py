
from django.shortcuts import render
from .models import Question


def index(request):
    question_list = Question.objects.order_by('-create_date')
    context = {'question_list': question_list}
    return render(request, 'pybo/question_list.html', context)

def detail(request, question_id):
    question = Question.objects.get(id=question_id)
    context = {'question': question}
    return render(request, 'pybo/question_detail.html', context)

def lay(request):
    return render(request, 'pybo/layout.html')


def lay2(request):
    return render(request, 'pybo/layout2.html')

def lay3(request):
    return render(request, 'pybo/layout3.html')

def lay4(request):
    question_list = Question.objects.order_by('-create_date')
    context = {'question_list': question_list}
    return render(request, 'pybo/layout4.html', context)