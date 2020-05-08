from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.urls import reverse
from django.utils import timezone
from .models import Board, Post

def index(req):
  offset = 0
  if "offset" in req.GET:
    try:
      offset = int(req.GET["offset"])
    except ValueError as err:
      pass
    
  return render(req, "imageboard/index.html", {
    "boards": Board.objects.order_by("-created_at")[offset:offset+20]
  })

def board(req, id):
  board = get_object_or_404(Board, pk=id)
    
  return render(req, "imageboard/board.html", {
    "board": board,
    "posts": Post.objects.all().filter(posted_to=board)
  })

def create_board(req):
  board = Board.objects.create(
    created_at=timezone.now(),
    title=req.POST["title"])
  post = Post.objects.create(
    created_at=timezone.now(),
    posted_to=board,
    author="名無しさん" if req.POST["author"] == "" else req.POST["author"],
    text=req.POST["text"])

  return HttpResponseRedirect(reverse("imageboard:board", args=(board.id,)))

def create_post(req, id):
  board = get_object_or_404(Board, pk=id)
  post = Post.objects.create(
    created_at=timezone.now(),
    posted_to=board,
    author="名無しさん" if req.POST["author"] == "" else req.POST["author"],
    text=req.POST["text"])

  return HttpResponseRedirect(reverse("imageboard:board", args=(board.id,)))
