from graphene import relay
from graphene_django import DjangoObjectType
from graphene_django_extras import (
    DjangoListObjectType, LimitOffsetGraphqlPagination,
)

from backend.template.models import Chart, Dimension, Metric, Pivot, Template


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


class TemplateType(DjangoObjectType):
    class Meta:
        model = Template


class TemplateNode(DjangoObjectType):
    class Meta:
        model = Template
        interfaces = (relay.Node,)
        fields = '__all__'
        filter_fields = {
            'name': ['icontains']}


class TemplateListType(DjangoListObjectType):
    class Meta:
        model = Template
        description = 'All reports'
        pagination = LimitOffsetGraphqlPagination(default_limit=6,
                                                  ordering="-name")
        filter_fields = {
            "id": ("exact",), "name": ("icontains", "iexact"), }


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


class TemplateConnection(relay.Connection):
    class Meta:
        node = TemplateNode
