from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.template import loader
from django.urls import reverse
from .models import Question, Choice

def index(req):
  latest_question_list = Question.objects.order_by("-pub_date")[:5]
  return render(req, "polls/index.html", {
    "latest_question_list": latest_question_list,
  })

def detail(req, question_id):
  question = get_object_or_404(Question, pk=question_id)
  return render(req, "polls/detail.html", {
    "title": "Q%s detail" % question_id,
    "question": question
  })

def result(req, question_id):
  question = get_object_or_404(Question, pk=question_id)
  return render(req, "polls/result.html", {
    "question": question
  })

def vote(req, question_id):
  question = get_object_or_404(Question, pk=question_id)
  try:
    print("Recieved Choice", req.POST["choice"])
    selected_choice = question.choice_set.get(pk=req.POST["choice"])
  except(KeyError, Choice.DoesNotExist):
    return render(req, "polls/detail.html", {
      "question": question,
      "error_message": "No choices selected."
    })
  else:
    selected_choice.votes += 1
    selected_choice.save()
    return HttpResponseRedirect(reverse("polls:result", args=(question.id,)))
