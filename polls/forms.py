"""
    forms.py
"""

from django import forms

class PollForm(forms.Form):
    title = forms.CharField(label='Poll title', max_length=100, required=True)
    question_amount = forms.IntegerField(label='Question amount', min_value=1, max_value=10, required=True)
    start_date = forms.DateField()
    end_date = forms.DateField()
