import graphene
from graphene import relay
from graphene_django.filter import DjangoFilterConnectionField
from graphql_relay import from_global_id

from backend.template.models import Chart, Dimension, Metric, Pivot, Template
from backend.template.schema.types import (ChartConnection, ChartType, DimensionConnection, DimensionType,
                                           MetricConnection, MetricType, PivotConnection, PivotType, TemplateNode)


class DimensionQuery:
    """ Query to get list of GA dimensions or single dimension """
    dimensions = relay.ConnectionField(DimensionConnection)
    dimension = graphene.Field(DimensionType, id=graphene.ID())

    def resolve_dimensions(root, info, **kwargs):
        """ Get list of dimension """
        return Dimension.objects.all()

    def resolve_dimension(root, info, id, **kwargs):
        """ Retrieve certain dimension """
        return Dimension.objects.filter(pk=id).first()


class MetricQuery:
    """ Query to get list of GA metrics or single metric """
    metrics = relay.ConnectionField(MetricConnection)
    metric = graphene.Field(MetricType, id=graphene.ID())

    def resolve_metrics(root, info, **kwargs):
        """ Get list of metrics """
        return Metric.objects.all()

    def resolve_metric(root, info, id, **kwargs):
        """ Retrieve certain metric"""
        return Metric.objects.filter(pk=id).first()


class PivotQuery:
    """ Query to get list of pivots or single pivot """
    pivots = relay.ConnectionField(PivotConnection)
    pivot = graphene.Field(PivotType, id=graphene.ID())

    def resolve_pivots(root, info, **kwargs):
        """ Get list of pivots """
        return Pivot.objects.all()

    def resolve_pivot(root, info, id, **kwargs):
        """ Retrieve single pivot """
        return Pivot.objects.filter(pk=id).first()


class ChartQuery:
    """ Query to get list of charts or single chart """
    charts = relay.ConnectionField(ChartConnection)
    chart = graphene.Field(ChartType, id=graphene.ID())

    def resolve_charts(root, info, **kwargs):
        """ Get list of charts """
        return Chart.objects.all()

    def resolve_chart(root, info, id, **kwargs):
        """ Retrieve certain chart """
        return Chart.objects.filter(pk=id).first()


class TemplateQuery:
    """ Get list of templates or single template
    Uses relay.Node interface
    Can be filtered by template name: nameIcontains: "searchname"

    """
    templates = DjangoFilterConnectionField(TemplateNode)
    template = relay.node.Field(TemplateNode, id=graphene.String())

    def resolve_template(root, info, id, **kwargs):
        """ Retrieve certain template
        id - must be a relay.Node id: str e.g.
            id: "VGVtcGxhdGVOb2RlOjE="
        """
        return Template.objects.filter(pk=from_global_id(id)[1]).first()
