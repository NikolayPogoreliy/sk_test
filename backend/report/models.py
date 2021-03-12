from django.db import models


class ReportStateChoices(models.IntegerChoices):
    ACTIVE = 1, 'Active'
    ARCHIVED = 2, 'Archived'
    DELETED = 4, 'Deleted'


class Report(models.Model):
    owner = models.ForeignKey('core.User', on_delete=models.PROTECT, related_name='user_reports')
    name = models.CharField(max_length=300)
    account = models.ForeignKey('core.Account', on_delete=models.CASCADE, related_name='account_reports')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    type = models.CharField(max_length=20)
    date_from = models.DateField()
    date_to = models.DateField()
    data = models.JSONField(default=dict)
    state = models.PositiveSmallIntegerField(choices=ReportStateChoices.choices, default=ReportStateChoices.ACTIVE)
