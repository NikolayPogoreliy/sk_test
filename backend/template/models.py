# Create your models here.
from django.db import models


# Create your models here.


class Chart(models.Model):
    name = models.CharField(blank=False, unique=True, max_length=300)
    metrics = models.ManyToManyField(to='Metric', related_name='chart_for_metric')
    dimension = models.ManyToManyField(to='Dimension', related_name='chart_for_dimension')
    pivot = models.ManyToManyField(to='Pivot', related_name='chart_for_pivot', null=True, blank=True)

    def __str__(self):
        return self.name


class Pivot(models.Model):
    name = models.CharField(max_length=50, unique=True)
    metrics = models.ManyToManyField(to='Metric', related_name='pivot_for_metric')
    dimension = models.ManyToManyField(to='Dimension', related_name='pivot_for_dimension')
    max_group_count = models.PositiveSmallIntegerField(default=10)
    start_group = models.PositiveSmallIntegerField(default=10)

    def __str__(self):
        return self.name


class Metric(models.Model):
    name = models.CharField(max_length=300, unique=True, blank=False)

    def __str__(self):
        return self.name


class Dimension(models.Model):
    name = models.CharField(max_length=300, unique=True, blank=False)

    def __str__(self):
        return self.name
