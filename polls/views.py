"""
    `views.py`
    Contains views of `polls` application
"""

import os

from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required, permission_required
from django.contrib.auth.models import User
from django.db import connection
from django.db.models import Count
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect
from polls.forms import *
from polls.models import *

def index(request):
    ''' Poll application index page '''
    # Get all `Poll` objects, add `question_count` attribute to each poll
    poll_list = Poll.objects.annotate(question_count=Count('question'))

    context = {
        'page_title': 'My Poll Page',
        'poll_list': poll_list,
    }

    return render(request, template_name='polls/index.html', context=context)

@login_required
@permission_required('polls.view_poll')
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

@login_required
@permission_required('polls.add_poll')
def create(request):
    ''' Poll application new poll creation page'''
    if request.method == 'POST':
        form = PollModelForm(request.POST)

        if form.is_valid():
            form.save()

            poll = Poll.objects.create(
                title=form.cleaned_data.get('title'),
                start_date=form.cleaned_data.get('start_date'),
                end_date=form.cleaned_data.get('end_date'),
            )

            for i in range(form.cleaned_data.get('question_amount')):
                Question.objects.create(
                    text='Question {:02d}'.format(i + 1),
                    type='01',
                    poll=poll
                )

            return redirect('index')
    else:
        form = PollModelForm()

    context = {
        'form': form,
        'error': form.error
    }

    return render(request, template_name='polls/create.html', context=context)

@login_required
@permission_required('polls.change_poll')
def edit(request, poll_id):
    poll = Poll.objects.get(pk=poll_id)

    if request.method == 'POST':
        form = PollModelForm(request.POST, instance=poll)

        if form.is_valid():
            form.save()

    else:
        form = PollModelForm(instance=poll)

    context = {
        'poll': poll,
        'form': form,
        'error': form.error
    }

    return render(request, template_name='polls/edit.html', context=context)

@login_required
def comment(request, poll_id):
    ''' Poll application comment page '''
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            print(form.cleaned_data)
            comment = Comment.objects.create(
                poll=Poll.objects.get(pk=poll_id),
                title=form.cleaned_data.get('title'),
                body=form.cleaned_data.get('body'),
                email=form.cleaned_data.get('email'),
                tel=form.cleaned_data.get('tel')
            )
            return redirect('detail', poll_id=poll_id)
    else:
        form = CommentForm()

    context = {
        'poll': Poll.objects.get(pk=poll_id),
        'form': form,
        'error': form.error,
    }

    return render(request, template_name='polls/comment.html', context=context)

def login_user(request):
    ''' Poll application login page '''
    context = {}

    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)

        if user:
            login(request, user)

            next_url = request.POST.get('next_url')
            if next_url:
                return redirect(next_url)
            else:
                return redirect('index')

        else:
            context['username'] = username
            context['password'] = password
            context['error'] = 'Incorrect username or password.'

    next_url = request.GET.get('next')
    if (next_url):
        context['next_url'] = next_url

    return render(request, template_name='polls/login.html', context=context)

def logout_user(request):
    ''' Poll application logout '''
    logout(request)
    return redirect('index')

@login_required
def change_password(request):
    ''' Poll application change password '''
    context = {}

    if request.method == 'POST':
        form = ChangePasswordForm(request.POST)
        if form.is_valid():
            user = User.objects.get(username=request.user.username)
            if authenticate(request, username=request.user.username, password=form.cleaned_data.get('password_old')):
                user.set_password(form.cleaned_data.get('password_new'))
                user.save()
            else:
                context['error'] = 'Incorrect Password.'
    else:
        form = ChangePasswordForm()

    context['form'] = form
    context['error'] = form.error

    return render(request, template_name='polls/change-password.html', context=context)

def register(request):
    ''' Poll application register '''
    context = {}

    if request.method == 'POST':
        form = RegisterForm(request.POST)

        if form.is_valid():
            user = User.objects.create(
                username=form.cleaned_data.get('username'),
                email=form.cleaned_data.get('email'),
            )
            user.set_password(form.cleaned_data.get('password'))
            user.save()

            Profile.objects.create(
                user=user,
                line_id=form.cleaned_data.get('line_id'),
                sex=form.cleaned_data.get('sex'),
                facebook=form.cleaned_data.get('facebook'),
                birth_date=form.cleaned_data.get('birth_date'),
            )
    else:
        form = RegisterForm()

    context['form'] = form
    context['error'] = form.error

    return render(request, template_name='polls/register.html', context=context)

# Non-view functions
def load_data_from_sql(file_name):
    ''' Utility function, executes SQL query from SQL file '''
    file_path = os.path.join(os.path.dirname(__file__), 'sql/', file_name)
    sql_statement = open(file_path).read()

    with connection.cursor() as cursor:
        cursor.execute(sql_statement)
