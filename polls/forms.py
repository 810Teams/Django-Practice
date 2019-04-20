"""
    forms.py
    Contains classes to create forms
"""

from django import forms
from django.core import validators
from django.core.exceptions import ValidationError

from polls.models import *

class PollForm(forms.ModelForm):
    # question_amount = forms.IntegerField(label='Question amount', min_value=1, max_value=15, required=True,
    #                                      widget=forms.NumberInput(attrs={'class' : 'form-control'}))

    class Meta:
        model = Poll
        exclude = ['del_flag']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'start_date': forms.DateInput(attrs={'class': 'form-control'}),
            'end_date': forms.DateInput(attrs={'class': 'form-control'}),
        }

    error = None

    def clean(self):
        data = super().clean()

        if len(data.get('title')) < 6:
            self.error = 'Title must be at least 6 characters long.'
            raise ValidationError('')
        elif (data.get('start_date') and not data.get('end_date')):
            self.error = 'Please fill end date.'
            raise ValidationError('')
        elif (not data.get('start_date') and data.get('end_date')):
            self.error = 'Please fill start date.'
            raise ValidationError('')
        else:
            self.error = None

class QuestionForm(forms.ModelForm):
    class Meta:
        model = Question
        exclude = ['poll']

        widgets = {
            'text': forms.TextInput(attrs={'class': 'form-control'}),
            'type': forms.Select(attrs={'class': 'form-control'}),
        }

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        exclude = []
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'body': forms.Textarea(attrs={'class': 'form-control'}),
            'email': forms.EmailInput(attrs={'class': 'form-control'}),
            'tel': forms.TextInput(attrs={'class': 'form-control'}),
        }

    error = None

    def clean(self):
        data = super().clean()

        if not (data.get('email') or data.get('tel')):
            self.error = 'Please fill email or telephone number.'
            raise ValidationError('')
        elif data.get('tel') and len(data.get('tel')) != 10:
            self.error = 'Telephone number length must be 10.'
            raise ValidationError('')
        else:
            self.error = None

class ChangePasswordForm(forms.Form):
    password_old = forms.CharField(max_length=255, required=True, widget=forms.PasswordInput(attrs={'class' : 'form-control'}))
    password_new = forms.CharField(max_length=255, required=True, widget=forms.PasswordInput(attrs={'class' : 'form-control'}))
    password_confirm = forms.CharField(max_length=255, required=True, widget=forms.PasswordInput(attrs={'class' : 'form-control'}))

    error = None

    def clean(self):
        cleaned_data = super().clean()

        if cleaned_data.get('password_new') != cleaned_data.get('password_confirm'):
            self.error = 'Password fields mismatch.'
            raise ValidationError('')
        elif len(cleaned_data.get('password_new')) < 8:
            self.error = 'New password must be at least 8 characters long.'
            raise ValidationError('')
        else:
            self.error = None

class RegisterForm(forms.ModelForm):
    username = forms.CharField(max_length=255, required=True,
                               widget=forms.NumberInput(attrs={'class' : 'form-control'}))
    password = forms.CharField(max_length=255, required=True,
                               widget=forms.PasswordInput(attrs={'class' : 'form-control'}))
    password_confirm = forms.CharField(max_length=100, required=True,
                                       widget=forms.PasswordInput(attrs={'class' : 'form-control'}))
    email = forms.EmailField(widget=forms.EmailInput(attrs={'class' : 'form-control'}))
    tel = forms.CharField(max_length=10, required=True, widget=forms.TextInput(attrs={'class' : 'form-control'}))

    class Meta:
        model = Profile
        exclude = ['user']
        widgets = {
            'line_id': forms.TextInput(attrs={'class': 'form-control'}),
            'facebook': forms.TextInput(attrs={'class': 'form-control'}),
            'sex': forms.Select(attrs={'class': 'form-control'}),
            'birth_date': forms.DateInput(attrs={'class': 'form-control'}),
        }

    error = None

    def clean(self):
        data = super().clean()

        if (data.get('password') != data.get('password_confirm')):
            self.error = 'Password fields mismatch.'
            raise ValidationError('')
        elif len(data.get('password')) < 8:
            self.error = 'Password must be at least 8 characters long.'
            raise ValidationError('')
        elif len(data.get('tel')) != 10:
            self.error = 'Telephone number length must be 10.'
            raise ValidationError('')
        else:
            self.error = None
