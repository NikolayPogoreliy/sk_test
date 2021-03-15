from math import ceil

import graphene
from graphene_django import DjangoObjectType

from backend.report.models import Report


class ReportType(DjangoObjectType):
    class Meta:
        model = Report


# class ReportConnection(graphene.relay.Connection):
#     class Meta:
#         node = ReportType


class ReportQuery:
    reports = graphene.List(ReportType)
    report = graphene.Field(ReportType, id=graphene.ID())

    def resolve_reports(self, info, **kwargs):
        qs = Report.objects.all()
        if 'filter' in kwargs:
            qs = qs.filter(**kwargs['filter'])
        if 'limit' in kwargs and 'page' in kwargs:
            limit = int(kwargs.get('limit', 15))
            if limit <= 0:
                limit = 15
            total_pages = int(ceil(qs.count() / limit))
            page = int(kwargs.get('page', 1))
            if page <= 0:
                page = 1
            if page > total_pages:
                page = total_pages

            from_row = limit * (page - 1)
            to_row = from_row + limit + 1
            qs = qs[from_row: to_row]
        return qs

    def resolve_report(self, info, id):
        report = Report.objects.filter(id=id)
        if report:
            return report.first()
        return Report.objects.none()
