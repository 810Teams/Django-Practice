"""
    forms.py
    Contains classes to create forms
"""

from django import forms
from django.core import validators
from django.core.exceptions import ValidationError


class PollForm(forms.Form):
    email = forms.CharField(validators=[validators.validate_email])
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
