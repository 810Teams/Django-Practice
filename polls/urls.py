"""
    `urls.py`
    Contains URLs in `polls` application
"""

from django.urls import path

from polls import views

urlpatterns = [
    path('index/', views.index, name='index'),
    path('detail/<int:poll_id>/', views.detail, name='detail'),
    path('create/', views.create, name='create'),
    path('login/', views.login_user, name='login'),
    path('logout/', views.logout_user, name='logout')
]
