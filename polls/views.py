from django.db.models import F
from django.http import HttpResponse, Http404, HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.template import loader
from django.urls import reverse

from polls.models import Question, Choice


def index(request):
    latest_questions_list = Question.objects.order_by("-pub_date")[:5]
    template = loader.get_template("polls/index.html")
    # output = ", ".join([q.question for q in latest_questions_list])
    # return HttpResponse(output)
    context = {"latest_question_list": latest_questions_list, }
    print(context)
    return HttpResponse(template.render(context, request))


def details_basic(request, question_id):
    return HttpResponse("Hello, world. You're looking at the question %s details view. " % question_id)


def results(request, question_id):
    response = "You're looking at the question %s results view." % question_id
    return HttpResponse(response % question_id)


def vote_old(request, question_id):
    return HttpResponse("You're looking at the question %s votes view." % question_id)


def details(request, question_id):
    # try:
    #     question = Question.objects.get(pk=question_id)
    # except Question.DoesNotExist:
    #     raise Http404("Question not found")
    question = get_object_or_404(Question, pk=question_id)

    context = {"question": question, }
    return render(request, "polls/detail.html", context)


def vote(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    try:
        selected_choice = question.choice_set.get(pk=request.POST["choice"])
    except (KeyError, Choice.DoesNotExist):
        return render(
            request,
            "polls/detail.html",
            {
                "question": question,
                "error_message": "You didn't select a choice.",
            },
        )

    else:
        selected_choice.votes = F("votes") + 1
        selected_choice.save()

        return HttpResponseRedirect(reverse("polls:results", args=(question.id,)))
