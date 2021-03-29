import graphene
from graphene_django.filter import DjangoFilterConnectionField
from graphql_relay import from_global_id

from backend.report.models import Report
from backend.report.schema.types import ReportType


class ReportQuery:
    """ Get list of reports or single report"""
    reports = DjangoFilterConnectionField(ReportType)
    report = graphene.Field(ReportType, id=graphene.String())

    def resolve_report(self, info, id):
        """ Retrieve certain report """
        report = Report.objects.filter(id=from_global_id(id)[1])
        if report:
            return report.first()
        return Report.objects.none()
