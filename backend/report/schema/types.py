from graphene_django import DjangoObjectType
from graphene_django_extras import DjangoListObjectType
from graphene_django_extras.paginations import LimitOffsetGraphqlPagination

from backend.report.models import Report


class ReportType(DjangoObjectType):
    class Meta:
        model = Report
        fields = '__all__'


class ReportListType(DjangoListObjectType):
    class Meta:
        model = Report
        fields = '__all__'
        description = 'All reports'
        pagination = LimitOffsetGraphqlPagination(default_limit=6,
                                                  ordering="-name")
        filter_fields = {
            "id": ("exact",), "name": ("icontains", "iexact"),
            "account_name": ("icontains", "iexact"), "account_id": ("exact",),
            "state": ("iexact",), }
