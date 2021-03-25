import graphene
from graphene import relay
from graphene_django import DjangoObjectType
from graphene_django.filter import DjangoFilterConnectionField
from graphql_relay import from_global_id

from backend.report.models import Report
from backend.vms.utils import get_analytics


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


class FilterType(graphene.ObjectType):
    name = graphene.String()
    account_id = graphene.Int()


class ReportQuery:
    reports = DjangoFilterConnectionField(ReportType)
    report = graphene.Field(ReportType, id=graphene.ID())

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
        report = Report.objects.filter(id=id)
        if report:
            return report.first()
        return Report.objects.none()


class CreateReport(graphene.Mutation):
    class Arguments:
        name = graphene.String()
        account_id = graphene.Int()
        account_name = graphene.String()
        type = graphene.String()
        date_from = graphene.types.Date()
        date_to = graphene.types.Date()
        template_id = graphene.String()

    report = graphene.Field(ReportType)

    def mutate(self, info, name, account_id, account_name, type, date_from, date_to, template_id):
        data = get_analytics(from_global_id(template_id)[1], date_from, date_to)
        report = Report.objects.create(
            name=name,
            account_id=account_id,
            account_name=account_name,
            type=type,
            date_from=date_from,
            date_to=date_to,
            data=data,
            owner=info.context.user
        )

        return CreateReport(report=report)


class UpdateReport(graphene.Mutation):
    class Arguments:
        id = graphene.String()
        name = graphene.String(required=False)
        date_from = graphene.types.Date(required=False)
        date_to = graphene.types.Date(required=False)
        data = graphene.JSONString(required=False)
        state = graphene.Int(required=False)

    report = graphene.Field(ReportType)

    def mutate(self, info, id, **kwargs):
        report = Report.objects.filter(id=from_global_id(id)[1])
        if report.exists():
            report.update(
                **kwargs
            )
        return UpdateReport(report=report.first())


class DeleteReport(graphene.Mutation):
    class Arguments:
        id = graphene.String()

    report = graphene.Field(ReportType)

    def mutate(self, info, id):
        report = Report.objects.filter(id=from_global_id(id)[1])
        report.delete()

        return DeleteReport(report=report.first())


class Mutation:
    create_report = CreateReport.Field()
    update_report = UpdateReport.Field()
    delete_report = DeleteReport.Field()
