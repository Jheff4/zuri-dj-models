from django.db import models
from django.conf import settings
from turtle import title
from django.contrib.auth import get_user_model
User = settings.AUTH_USER_MODEL

# Create your models here.
class Post(models.Model):
  Title = models.CharField(max_length=200)
  Text = models.TextField()
  Author = models.ForeignKey(get_user_model)
  created_date = models.DateTimeField()
  Published_date = models.DateTimeField()