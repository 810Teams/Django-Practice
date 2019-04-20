"""
    `urls.py`
    Contains URLs in `polls` application
"""

from django.urls import path

from polls import views

urlpatterns = [
    path('index/', views.index, name='index'),
    path('create/', views.create, name='create'),
    path('detail/<int:poll_id>/', views.detail, name='detail'),
    path('edit/<int:poll_id>/', views.edit, name='edit'),
    path('detail/<int:poll_id>/comment/', views.comment, name='comment'),
    path('login/', views.login_user, name='login'),
    path('logout/', views.logout_user, name='logout'),
    path('change-password/', views.change_password, name='change-password'),
    path('register/', views.register, name='register'),
]
