import graphene
from graphene_django.filter import DjangoFilterConnectionField
from graphql_relay import from_global_id

from backend.report.models import Report
from backend.report.schema.types import ReportType


class ReportQuery:
    reports = DjangoFilterConnectionField(ReportType)
    report = graphene.Field(ReportType, id=graphene.String())

    # def resolve_reports(self, info, **kwargs):
    #     return Report.objects.all()
    #     if 'limit' in kwargs and 'page' in kwargs:
    #         limit = int(kwargs.get('limit', 15))
    #         if limit <= 0:
    #             limit = 15
    #         total_pages = int(ceil(qs.count() / limit))
    #         page = int(kwargs.get('page', 1))
    #         if page <= 0:
    #             page = 1
    #         if page > total_pages:
    #             page = total_pages
    #
    #         from_row = limit * (page - 1)
    #         to_row = from_row + limit + 1
    #         qs = qs[from_row: to_row]
    #     return qs

    def resolve_report(self, info, id):
        report = Report.objects.filter(id=from_global_id(id)[1])
        if report:
            return report.first()
        return Report.objects.none()
