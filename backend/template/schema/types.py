from graphene import relay
from graphene_django import DjangoObjectType

from backend.template.models import Chart, Dimension, Metric, Pivot


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
