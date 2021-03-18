# Register your models here.
from django.contrib import admin

from backend.template.models import Dimension, Metric, Pivot, Chart

admin.site.register(Dimension)
admin.site.register(Metric)
admin.site.register(Pivot)
admin.site.register(Chart)
