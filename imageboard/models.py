from django.db import models

class Board(models.Model):
  created_at = models.DateTimeField()
  title = models.CharField(max_length=50)

class Post(models.Model):
  created_at = models.DateTimeField()
  posted_to = models.ForeignKey(Board, on_delete=models.CASCADE, null=True)
  author = models.CharField(max_length=20, default="名無しさん")
  text = models.TextField()
