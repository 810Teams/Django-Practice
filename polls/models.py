"""
    `models.py`
    Contains database model of `polls` application
"""

from django.db import models

class Poll(models.Model):
    title = models.CharField(max_length=255)
    start_date = models.DateField(null=True, blank=True)
    end_date = models.DateField(null=True, blank=True)
    del_flag = models.BooleanField(default=False)

    def __str__(self):
        return '{}'.format(self.title)

class Question(models.Model):
    TYPES = (
        ('01', 'Single answer'),
        ('02', 'Multiple answers'),
    )

    text = models.CharField(max_length=255)
    type = models.CharField(max_length=2, choices=TYPES, default='01')
    poll = models.ForeignKey(Poll, on_delete=models.CASCADE)

    def __str__(self):
        return '{} - {}'.format(self.poll.title, self.text)

class Choice(models.Model):
    text = models.CharField(max_length=255)
    value = models.IntegerField(default=0)
    question = models.ForeignKey(Question, on_delete=models.CASCADE)

    def __str__(self):
        return '{} - {}'.format(self.question, self.text)

class Answer(models.Model):
    choice = models.OneToOneField(Choice, on_delete=models.CASCADE)
    question = models.ForeignKey(Question, on_delete=models.CASCADE)

class Comment(models.Model):
    poll = models.ForeignKey(Poll, on_delete=models.CASCADE, default=None)
    title = models.CharField(max_length=100)
    body = models.TextField()
    email = models.EmailField()
    tel = models.CharField(max_length=10)

class Profile(models.Model):
    SEX = (
        ('M', 'Male'),
        ('F', 'Female'),
        ('X', 'Others')
    )

    user = models.OneToOneField('auth.User', on_delete=models.CASCADE)
    line_id = models.CharField(max_length=255, null=True, blank=True)
    facebook = models.CharField(max_length=255, null=True, blank=True)
    sex = models.CharField(max_length=1, choices=SEX)
    birth_date = models.DateField(null=True)
