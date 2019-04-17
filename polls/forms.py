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

    def clean_title(self):
        data = self.cleaned_data['title']

        if len(data) < 6:
            raise ValidationError('Title is too short!')

        return data

    def clean(self):
        cleaned_data = super().clean()
        start = cleaned_data.get('start_date')
        end = cleaned_data.get('end_date')

        if (start and not end):
            self.add_error('end_date', 'Please fill end date.')
            # raise ValidationError('Please fill end date.')

        elif (not start and end):
            self.add_error('start_date', 'Please fill start date.')
            # raise ValidationError('Please fill start date.')

class CommentForm(forms.Form):
    title = forms.CharField(max_length=100, required=True)
    body = forms.CharField(max_length=500, required=True)
    email = forms.EmailField(required=False)
    tel = forms.CharField(max_length=10, required=False)

    def clean(self):
        cleaned_data = super().clean()

        if not (cleaned_data.get('email') or cleaned_data.get('tel')):
            raise ValidationError('Please fill email or tel')

        if cleaned_data.get('tel') and len(cleaned_data.get('tel')) != 10:
            raise ValidationError('Tel length must be 10')

class ChangePasswordForm(forms.Form):
    password_old = forms.CharField(max_length=100, required=True, widget=forms.PasswordInput)
    password_new = forms.CharField(max_length=100, required=True, widget=forms.PasswordInput)
    password_confirm = forms.CharField(max_length=100, required=True, widget=forms.PasswordInput)

    def clean(self):
        cleaned_data = super().clean()

        if cleaned_data.get('password_new') != cleaned_data.get('password_confirm'):
            raise ValidationError('Password mismatch')

        if len(cleaned_data.get('password_new')) < 8:
            raise ValidationError('Password too short')

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

    def clean(self):
        cleaned_data = super().clean()

        if (cleaned_data.get('password') != cleaned_data.get('password_confirm')):
            raise ValidationError('Password mismatch')
        if len(cleaned_data.get('password')) < 8:
            raise ValidationError('Password too short')
        if len(cleaned_data.get('tel')) != 10:
            raise ValidationError('Tel length must be 10')

