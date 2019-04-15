import os

from django.db.models import Count
from django.http import HttpResponse
from django.shortcuts import render
from django.db import connection

# Create your views here.

from polls.models import Poll, Question

def index(request):
    # load_data_from_sql('polls_preset.sql')

    # Get all `Poll` objects, add `question_count` attribute to each poll
    poll_list = Poll.objects.annotate(question_count=Count('question')).filter(question_count__gt=0)

    context = {
        'page_title': 'Welcome to my poll page',
        'poll_list': poll_list,
    }

    return render(request, template_name='polls/index.html', context=context)

def detail(request, poll_id):
    poll = Poll.objects.get(pk=poll_id)

    context = {
        'poll': poll
    }

    return render(request, template_name='polls/detail.html', context=context)

# Non-view functions
def load_data_from_sql(file_name):
    file_path = os.path.join(os.path.dirname(__file__), 'sql/', file_name)
    sql_statement = open(file_path).read()

    with connection.cursor() as cursor:
        cursor.execute(sql_statement)
