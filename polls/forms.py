"""
    forms.py
    Contains classes to create forms
"""

from django import forms
from django.contrib.auth import authenticate
from django.core import validators
from django.core.exceptions import ValidationError

class PollForm(forms.Form):
    title = forms.CharField(label='Poll title', max_length=100, required=True)
    question_amount = forms.IntegerField(label='Question amount', min_value=1, max_value=10, required=True)
    start_date = forms.DateField(required=False)
    end_date = forms.DateField(required=False)

    error = None

    def clean(self):
        cleaned_data = super().clean()

        start = cleaned_data.get('start_date')
        end = cleaned_data.get('end_date')

        if len(cleaned_data.get('title')) < 6:
            self.error = 'Title must be at least 6 characters long.'
            raise ValidationError('')
        elif (start and not end):
            self.error = 'Please fill end date.'
            raise ValidationError('')
        elif (not start and end):
            self.error = 'Please fill start date.'
            raise ValidationError('')
        else:
            self.error = None

class CommentForm(forms.Form):
    title = forms.CharField(max_length=100, required=True)
    body = forms.CharField(max_length=500, required=True)
    email = forms.EmailField(required=False)
    tel = forms.CharField(max_length=10, required=False)

    error = None

    def clean(self):
        cleaned_data = super().clean()

        if not (cleaned_data.get('email') or cleaned_data.get('tel')):
            self.error = 'Please fill email or telephone number.'
            raise ValidationError('')
        elif cleaned_data.get('tel') and len(cleaned_data.get('tel')) != 10:
            self.error = 'Telephone number length must be 10.'
            raise ValidationError('')
        else:
            self.error = None

class ChangePasswordForm(forms.Form):
    password_old = forms.CharField(max_length=100, required=True, widget=forms.PasswordInput)
    password_new = forms.CharField(max_length=100, required=True, widget=forms.PasswordInput)
    password_confirm = forms.CharField(max_length=100, required=True, widget=forms.PasswordInput)

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

class RegisterForm(forms.Form):
    SEX = (
        ('M', 'Male'),
        ('F', 'Female'),
        ('X', 'Others')
    )

    username = forms.CharField(max_length=100, required=True)
    password = forms.CharField(max_length=100, required=True, widget=forms.PasswordInput)
    password_confirm = forms.CharField(max_length=100, required=True, widget=forms.PasswordInput)
    email = forms.EmailField()
    tel = forms.CharField(max_length=10, required=True)
    line_id = forms.CharField(max_length=100, required=False)
    facebook = forms.CharField(max_length=100, required=False)
    sex = forms.ChoiceField(choices=SEX, widget=forms.RadioSelect, required=True)
    birth_date = forms.DateField(required=False)

    error = None

    def clean(self):
        cleaned_data = super().clean()

        if (cleaned_data.get('password') != cleaned_data.get('password_confirm')):
            self.error = 'Password fields mismatch.'
            raise ValidationError('')
        elif len(cleaned_data.get('password')) < 8:
            self.error = 'Password must be at least 8 characters long.'
            raise ValidationError('')
        elif len(cleaned_data.get('tel')) != 10:
            self.error = 'Telephone number length must be 10.'
            raise ValidationError('')
        else:
            self.error = None
