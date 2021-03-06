from django.http import HttpResponse
from django.shortcuts import render


def index(request):
    return HttpResponse("Hello World")


def detail(request, question_id):
    x = question_id
    print(x)
    return HttpResponse(f"You're looking at question {question_id}.")


def results(request, question_id):
    response = "You're looking at the results of question %s."
    return HttpResponse(response % question_id)


def vote(request, question_id):
    return HttpResponse("You're voting on question %s." % question_id)
