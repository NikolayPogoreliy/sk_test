# Register your models here.
from django.contrib import admin

from backend.template.models import Chart, Dimension, Metric, Pivot, Template

admin.site.register(Dimension)
admin.site.register(Metric)
admin.site.register(Pivot)
admin.site.register(Chart)
admin.site.register(Template)
