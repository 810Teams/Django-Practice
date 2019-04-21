"""
    `urls.py`
    Contains URLs in `polls` application
"""

from django.urls import path

from polls import views

urlpatterns = [
    path('', views.index, name='index'),
    path('poll/create/', views.create_poll, name='create-poll'),
    path('poll/<int:poll_id>/', views.poll, name='poll'),
    path('poll/<int:poll_id>/edit', views.edit_poll, name='edit-poll'),
    path('poll/<int:poll_id>/comment/', views.comment, name='comment'),
    path('question/<int:question_id>/edit-choice/', views.edit_choice, name='edit-choice'),
    path('question/<int:question_id>/edit-choice/api/', views.edit_choice_api, name='edit-choice-api'),
    path('question/<int:question_id>/delete', views.delete_question, name='delete-question'),
    path('login/', views.login_user, name='login'),
    path('logout/', views.logout_user, name='logout'),
    path('change-password/', views.change_password, name='change-password'),
    path('register/', views.register, name='register'),
]
