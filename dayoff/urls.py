"""
    `urls.py`
    Contains URLs in `polls` application
"""

from django.urls import path

from dayoff import views

urlpatterns = [
    path('', views.index, name='index'),
    path('create/', views.create, name='create-dayoff')
]
