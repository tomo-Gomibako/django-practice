from django.urls import path

from . import views

app_name = "imageboard"
urlpatterns = [
  path("", views.index, name="index"),
  path("board/<int:id>", views.board, name="board"),
  path("create_board", views.create_board, name="create_board"),
  path("create_post/<int:id>", views.create_post, name="create_post")
]
