from django.db import models

# Create your models here.

class Poll(models.Model):
    title = models.CharField(max_length=100)
    start_date = models.DateField(null=True, blank=True)
    end_date = models.DateField(null=True, blank=True)
    del_flag = models.BooleanField(default=False)

class Question(models.Model):
    SINGLE = '01'
    MULTIPLE = '02'
    TYPES = (
        (SINGLE, 'Single answer'),
        (MULTIPLE, 'Multiple answers'),
    )

    text = models.TextField()
    type = models.CharField(max_length=2, choices=TYPES, default=SINGLE)
    poll = models.ForeignKey(Poll, on_delete=models.PROTECT)

class Choice(models.Model):
    text = models.CharField(max_length=100)
    value = models.IntegerField(default=0)
    question = models.ForeignKey(Question, on_delete=models.PROTECT)

class Answer(models.Model):
    choice = models.OneToOneField(Choice, on_delete=models.PROTECT)
    question = models.ForeignKey(Question, on_delete=models.PROTECT)
