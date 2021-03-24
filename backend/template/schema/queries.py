import graphene
from graphene import relay

from backend.template.models import Chart, Dimension, Metric, Pivot, Template
from backend.template.schema.types import (ChartConnection, ChartType, DimensionConnection, DimensionType,
                                           MetricConnection, MetricType, PivotConnection, PivotType, TemplateConnection,
                                           TemplateType)


class DimensionQuery:
    dimensions = relay.ConnectionField(DimensionConnection)
    dimension = graphene.Field(DimensionType, id=graphene.ID())

    def resolve_dimensions(root, info, **kwargs):
        return Dimension.objects.all()

    def resolve_dimension(root, info, id, **kwargs):
        return Dimension.objects.filter(pk=id).first()


class MetricQuery:
    metrics = relay.ConnectionField(MetricConnection)
    metric = graphene.Field(MetricType, id=graphene.ID())

    def resolve_metrics(root, info, **kwargs):
        return Metric.objects.all()

    def resolve_metric(root, info, id, **kwargs):
        return Metric.objects.filter(pk=id).first()


class PivotQuery:
    pivots = relay.ConnectionField(PivotConnection)
    pivot = graphene.Field(PivotType, id=graphene.ID())

    def resolve_pivots(root, info, **kwargs):
        return Pivot.objects.all()

    def resolve_pivot(root, info, id, **kwargs):
        return Pivot.objects.filter(pk=id).first()


class ChartQuery:
    charts = relay.ConnectionField(ChartConnection)
    chart = graphene.Field(ChartType, id=graphene.ID())

    def resolve_charts(root, info, **kwargs):
        return Chart.objects.all()

    def resolve_chart(root, info, id, **kwargs):
        return Chart.objects.filter(pk=id).first()


class TemplateQuery:
    templates = relay.ConnectionField(TemplateConnection)
    template = graphene.Field(TemplateType, id=graphene.ID())

    def resolve_templates(root, info, **kwargs):
        return Template.objects.all()

    def resolve_template(root, info, id, **kwargs):
        return Template.objects.filter(pk=id).first()
