from __future__ import unicode_literals

from django.http import HttpResponse,HttpResponseRedirect
from django.http import Http404
from django.urls import reverse
from django.shortcuts import get_object_or_404
from django.shortcuts import render
from .models import Choice, Question,RegModel
from django import forms
from django.http import HttpResponseRedirect
from .forms import *
from django.contrib.auth import authenticate

def index(request):
    latest_question_list = Question.objects.all()
    context = {'latest_question_list': latest_question_list}
    return render(request, 'polls/index.html', context)

def detail(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    return render(request, 'polls/detail.html', {'question': question})


def vote(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    try:
        selected_choice = question.choice_set.get(pk=request.POST['choice'])
    except (KeyError, Choice.DoesNotExist):
        return render(request, 'polls/detail.html', {
            'question': question,
            'error_message': "You didn't select a choice.",
        })
    else:
        selected_choice.votes += 1
        selected_choice.save()
        return HttpResponseRedirect(reverse('polls:results', args=(question.id,)))

def results(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    return render(request, 'polls/results.html', {'question': question})


def create(request):
    if request.method == "POST":
        form = QuestionForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/polls/')
    else:
        form = QuestionForm()

    return render(request, "polls/create.html", {'form': form})
   
def forms(request):
    if request.method=="POST":
        form = NewForm(request.POST)
        if form.is_valid():
            return HttpResponseRedirect('/polls/')
    else:
        form = NewForm()
        return render(request,'polls/new_form.html',{'form':form})

def registration(request):
    #import pdb;pdb.set_trace()
    if request.method=="POST":
        form = RegForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/polls/')
    else:
        form = RegForm()
    return render(request,"polls/regform.html",{'form':form})

