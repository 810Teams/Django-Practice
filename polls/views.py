from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.

from polls.models import Poll

def index(request):
    # poll_list = [
    #     {'id': 1, 'title': 'Web Programming'},
    #     {'id': 2, 'title': 'Web Technology'},
    #     {'id': 3, 'title': 'Multimedia Technology'},
    # ]
    #

    poll_list = Poll.objects.all()

    context = {
        'page_title': 'Welcome to my poll page',
        'poll_list': poll_list,
    }

    return render(request, template_name='polls/index.html', context=context)

def detail(request, poll_id):
    return HttpResponse('Hello, this is detail page of poll number %i' % poll_id)
