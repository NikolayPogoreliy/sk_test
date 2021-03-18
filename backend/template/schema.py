import graphene
from graphene import relay
from graphene_django import DjangoObjectType

from backend.template.models import Metric, Dimension, Pivot, Chart


class MetricType(DjangoObjectType):
    class Meta:
        model = Metric
        interface = (relay.Node,)
        fields = '__all__'


class DimensionType(DjangoObjectType):
    class Meta:
        model = Dimension
        interface = (relay.Node,)
        fields = '__all__'


class PivotType(DjangoObjectType):
    class Meta:
        model = Pivot
        interface = (relay.Node,)
        fields = '__all__'


class ChartType(DjangoObjectType):
    class Meta:
        model = Chart
        interface = (relay.Node,)
        fields = '__all__'


class DimensionConnection(relay.Connection):
    class Meta:
        node = DimensionType


class MetricConnection(relay.Connection):
    class Meta:
        node = MetricType


class PivotConnection(relay.Connection):
    class Meta:
        node = PivotType


class ChartConnection(relay.Connection):
    class Meta:
        node = ChartType


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
