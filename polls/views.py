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
from django.forms import formset_factory
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from django.shortcuts import render, redirect
from django.views.decorators.csrf import csrf_exempt

from polls.forms import *
from polls.models import *

import json

def index(request):
    ''' Poll application index page '''
    # Get all `Poll` objects, add `question_count` attribute to each poll
    poll_list = Poll.objects.annotate(question_count=Count('question'))

    context = {
        'poll_list': poll_list,
    }

    return render(request, template_name='polls/index.html', context=context)

@login_required
@permission_required('polls.view_poll')
def poll(request, poll_id):
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

    return render(request, template_name='polls/poll.html', context=context)

@login_required
@permission_required('polls.add_poll')
def create_poll(request):
    ''' Poll application new poll creation page'''
    QuestionFormset = formset_factory(QuestionForm, min_num=1, max_num=15, extra=0)

    if request.method == 'POST':
        form = PollForm(request.POST)
        formset = QuestionFormset(request.POST)

        if form.is_valid():
            poll = form.save()
            if formset.is_valid():
                for i in formset:
                    Question.objects.create(
                        text=i.cleaned_data.get('text'),
                        type=i.cleaned_data.get('type'),
                        poll=poll
                    )
                return redirect('index')
    else:
        form = PollForm()
        formset = QuestionFormset()

    context = {
        'form': form,
        'formset': formset,
        'error': form.error
    }

    return render(request, template_name='polls/create-poll.html', context=context)

@login_required
@permission_required('polls.change_poll')
def edit_poll(request, poll_id):
    ''' Poll application edit poll page'''
    QuestionFormset = formset_factory(QuestionForm)
    poll = Poll.objects.get(pk=poll_id)

    if request.method == 'POST':
        form = PollForm(request.POST, instance=poll)
        formset = QuestionFormset(request.POST)

        if form.is_valid():
            form.save()

            if formset.is_valid():
                for i in formset:
                    if i.cleaned_data.get('question_id'):
                        question = Question.objects.get(id=i.cleaned_data.get('question_id'))

                        if question:
                            question.text = i.cleaned_data.get('text')
                            question.type = i.cleaned_data.get('type')
                            question.save()
                    elif i.cleaned_data.get('text'):
                        Question.objects.create(
                            text=i.cleaned_data.get('text'),
                            type=i.cleaned_data.get('type'),
                            poll=poll
                        )
                return redirect('edit-poll', poll_id=poll_id)

    else:
        form = PollForm(instance=poll)
        formset = QuestionFormset(initial=[{'text': i.text, 'type': i.type, 'question_id': i.id}
                                           for i in poll.question_set.all()])

    context = {
        'poll': poll,
        'form': form,
        'formset': formset,
        'error': form.error
    }

    return render(request, template_name='polls/edit-poll.html', context=context)

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
            return redirect('poll', poll_id=poll_id)
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
def edit_choice(request, question_id):
    question = Question.objects.get(pk=question_id)

    choices = [{'id': i.id, 'text': i.text, 'value': i.value, 'question': i.question_id}
               for i in question.choice_set.all()]

    context = {
        'poll': question.poll,
        'question': question,
        'choices': json.dumps(choices),
    }

    return render(request, template_name='polls/edit-choice.html', context=context)

@csrf_exempt
def edit_choice_api(request, question_id):
    if request.method == 'POST':
        choice_list = json.loads(request.body)
        error_message = None

        # Delete choices
        old_choices = [{'id': i.id, 'text': i.text, 'value': i.value, 'question': i.question_id}
                       for i in Question.objects.get(pk=question_id).choice_set.all()]
        for i in old_choices:
            if i not in choice_list:
                Choice.objects.get(pk=i['id']).delete()

        # Save choices
        for i in choice_list:
            data = {
                'text': i['text'],
                'value': i['value'],
                'question': question_id,
            }

            try:
                # If choice already exists
                if i['text'] == '' or i['value'] == None:
                    error_message = 'Fields can\'t be left blank.'
                    break
                Choice.objects.filter(pk=i['id']).update(text=i['text'], value=i['value'])
            except KeyError:
                # If choice not found
                form = ChoiceForm(data)
                if form.is_valid():
                    form.save()
                else:
                    error_message = 'Fields can\'t be left blank.'

        if not error_message:
            return JsonResponse({'message': 'success'}, status=200)
        return JsonResponse({'message': error_message}, status=400)
    return JsonResponse({'message': 'This API doesn\'t accept GET requests.'}, status=405)

@login_required
def delete_question(request, question_id):
    question = Question.objects.get(pk=question_id)
    question.delete()

    return redirect('edit-poll', poll_id=question.poll.id)

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
                return redirect('index')
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

            return redirect('index')
    else:
        form = RegisterForm()

    context['form'] = form
    context['error'] = form.error

    return render(request, template_name='polls/register.html', context=context)

def load_preset(file_name='polls_preset.sql'):
    ''' Utility function, executes SQL query from SQL file '''
    file_path = os.path.join(os.path.dirname(__file__), 'sql/', file_name)
    sql_statement = open(file_path).read()

    with connection.cursor() as cursor:
        cursor.execute(sql_statement)
