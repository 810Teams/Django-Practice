"""
    admin.py
"""

from django.contrib import admin
from django.contrib.auth.models import Permission
from polls.models import Poll, Question, Choice, Comment

class QuestionInline(admin.StackedInline):
    model = Question
    extra = 1

class ChoiceInline(admin.TabularInline):
    model = Choice
    extra = 2

class PollAdmin(admin.ModelAdmin):
    list_filter = ['start_date', 'end_date', 'del_flag']
    list_display = ['id', 'title', 'start_date', 'end_date', 'del_flag']
    list_per_page = 20
    search_fields = ['title']

    # fields = ['title', 'start_date', 'end_date']
    # exclude = ['del_flag']
    fieldsets = [
        (None, {'fields': ['title',
                           'del_flag']}),
        ('Active Duration', {'fields': ['start_date',
                                        'end_date'],
                             'classes': ['collapse']})
    ]

    inlines = [QuestionInline]

class QuestionAdmin(admin.ModelAdmin):
    list_filter = ['poll']
    list_display = ['id', 'text', 'type', 'poll']
    list_per_page = 20

    inlines = [ChoiceInline]

class ChoiceAdmin(admin.ModelAdmin):
    list_filter = ['question']
    list_display = ['id', 'text', 'value', 'question']
    list_per_page = 20

class CommentAdMin(admin.ModelAdmin):
    list_filter = ['poll']
    list_display = ['id', 'title', 'email', 'tel', 'poll']
    search_fields = ['title']


admin.site.register(Permission)
admin.site.register(Poll, PollAdmin)
admin.site.register(Question, QuestionAdmin)
admin.site.register(Choice, ChoiceAdmin)
admin.site.register(Comment, CommentAdMin)
