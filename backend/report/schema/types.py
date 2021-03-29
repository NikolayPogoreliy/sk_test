from graphene import relay
from graphene_django import DjangoObjectType

from backend.report.models import Report


class ReportType(DjangoObjectType):
    class Meta:
        model = Report
        interfaces = (relay.Node,)
        fields = '__all__'
        filter_fields = {
            'name': ['icontains'],
            'account_id': ['exact'],
            'account_name': ['icontains']
        }
