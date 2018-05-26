from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User


class Question(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')
    def __str__(self):
        return self.question_text


class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)
    def __str__(self):
        return self.choice_text

class RegModel(models.Model):
    user = models.OneToOneField(User)
    def __str__(self):
        return self.user.username

TITLE_CHOICES = (
    ('MR','Mr.'),
    ('MRS','Mrs.'),
    ('MS','Ms.'),
)
class Author(models.Model):
    name = models.CharField(max_length=100)
    title = models.CharField(max_length=3,choices = TITLE_CHOICES)
    birth_date = models.DateField(blanl=True,null=True)
    def __str__(self):
        return self.name