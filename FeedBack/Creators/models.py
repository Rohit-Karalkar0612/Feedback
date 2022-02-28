from django.db import models
from User.models import New
from django.contrib.auth.models import User

# Create your models here.
class Event(models.Model):
    creator = models.ForeignKey(
        New, related_name='create', on_delete=models.CASCADE)
    csv_file = models.FileField(upload_to='documents')
    pdf_file = models.FileField(upload_to='documents')

class Question(models.Model):
    question = models.CharField(max_length=200)
    event_related = models.ForeignKey(
        Event, related_name='event1', on_delete=models.CASCADE)

class Answer(models.Model):
    answer = models.CharField(max_length=300)
    answer_of_quest = models.ForeignKey(
        Question, related_name='answer1', on_delete=models.CASCADE)
    user_admin = models.ForeignKey(
        User, related_name='user1', on_delete=models.CASCADE)

