from django.db import models
from django.contrib.auth.models import User, Permission, Group

# Create your models here.

class DayOff(models.Model):
    TYPE_CHOICES = (
        ('01', 'Errand Leave'),
        ('02', 'Sick Leave')
    )

    APPROVE_STATUS_CHOICES = (
        (0, 'Rejected'),
        (1, 'Approved'),
        (2, 'Waiting')
    )

    reason = models.TextField(null=False, blank=False)
    type = models.CharField(max_length=2, choices=TYPE_CHOICES, null=False, blank=False)
    date_start = models.DateField(null=False, blank=False)
    date_end = models.DateField(null=False, blank=False)
    approve_status = models.IntegerField(choices=APPROVE_STATUS_CHOICES, default=2)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE, default=None)
