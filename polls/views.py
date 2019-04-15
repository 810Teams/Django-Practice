"""
    `views.py`
    Contains views of `polls` application
"""

import os

from django.db import connection
from django.db.models import Count
from django.http import HttpResponse
from django.shortcuts import render

from polls.models import Poll, Question, Answer

def index(request):
    ''' Poll application index page '''
    # Get all `Poll` objects, add `question_count` attribute to each poll
    poll_list = Poll.objects.annotate(question_count=Count('question')).filter(question_count__gt=0)

    context = {
        'page_title': 'Welcome to my poll page',
        'poll_list': poll_list,
    }

    return render(request, template_name='polls/index.html', context=context)

def detail(request, poll_id):
    ''' Poll application detail page '''
    poll = Poll.objects.get(pk=poll_id)

    context = {
        'poll': poll
    }

    # Notes: This will only be executed when receive `POST` request.
    if request.method == 'POST':
        for question in poll.question_set.all():
            choice_id = request.POST.get('question_' + str(question.id))

            if (choice_id != None):
                try:
                    answer = Answer.objects.get(question_id=question.id)
                    answer.choice_id = choice_id
                    answer.save()
                except Answer.DoesNotExist:
                    Answer.objects.create(choice_id=choice_id, question_id=question.id)

    return render(request, template_name='polls/detail.html', context=context)

# Non-view functions
def load_data_from_sql(file_name):
    ''' Utility function, executes SQL query from SQL file '''
    file_path = os.path.join(os.path.dirname(__file__), 'sql/', file_name)
    sql_statement = open(file_path).read()

    with connection.cursor() as cursor:
        cursor.execute(sql_statement)
