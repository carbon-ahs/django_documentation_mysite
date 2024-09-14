from django.http import HttpResponse
from django.shortcuts import render
from django.template import loader

from polls.models import Question


def index(request):
    latest_questions_list = Question.objects.order_by("-pub_date")[:5]
    template = loader.get_template("polls/index.html")
    # output = ", ".join([q.question for q in latest_questions_list])
    # return HttpResponse(output)
    context = {"latest_question_list": latest_questions_list, }
    print(context)
    return HttpResponse(template.render(context, request))


def details(request, question_id):
    return HttpResponse("Hello, world. You're looking at the question %s details view." % question_id)


def results(request, question_id):
    response = "You're looking at the question %s results view." % question_id
    return HttpResponse(response % question_id)


def vote(request, question_id):
    return HttpResponse("You're looking at the question %s votes view." % question_id)
