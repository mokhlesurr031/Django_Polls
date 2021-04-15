from django.db import models as db
import datetime
from django.utils import timezone


class Question(db.Model):
    question_text = db.CharField(max_length=200)
    pub_date = db.DateTimeField('date published')


    def was_published_recently(self):
        return self.pub_date >= timezone.now() - datetime.timedelta(days=1)

    def __str__(self):
        return self.question_text


class Choice(db.Model):
    question = db.ForeignKey(Question, on_delete=db.CASCADE)
    choice_text = db.CharField(max_length=200)
    votes = db.IntegerField(default=0)

    def __str__(self):
        return self.choice_text
