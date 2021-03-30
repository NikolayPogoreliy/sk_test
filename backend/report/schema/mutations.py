import graphene

from backend.report.models import Report
from backend.report.schema.types import ReportType
from backend.vms.utils import get_analytics


class CreateReport(graphene.Mutation):
    """ Create report """

    class Arguments:
        name = graphene.String()
        account_id = graphene.Int()
        account_name = graphene.String()
        type = graphene.String()
        date_from = graphene.types.Date()
        date_to = graphene.types.Date()
        template_id = graphene.ID()

    report = graphene.Field(ReportType)

    def mutate(self, info, name, account_id, account_name, type, date_from,
            date_to, template_id):
        data = get_analytics(template_id, date_from, date_to)
        report = Report.objects.create(name=name, account_id=account_id,
            account_name=account_name, type=type, date_from=date_from,
            date_to=date_to, data=data, owner=info.context.user)

        return CreateReport(report=report)


class UpdateReport(graphene.Mutation):
    """ Update report
    update name, date period, state and report data
    """

    class Arguments:
        id = graphene.String()
        name = graphene.String(required=False)
        date_from = graphene.types.Date(required=False)
        date_to = graphene.types.Date(required=False)
        data = graphene.JSONString(required=False)
        state = graphene.Int(required=False)

    report = graphene.Field(ReportType)

    def mutate(self, info, id, **kwargs):
        report = Report.objects.filter(id=id)
        if report.exists():
            report.update(
                **kwargs
            )
        return UpdateReport(report=report.first())


class DeleteReport(graphene.Mutation):
    """ Delete report """

    class Arguments:
        id = graphene.ID()

    report = graphene.Field(ReportType)

    def mutate(self, info, id):
        report = Report.objects.filter(id=id)
        report.delete()

        return DeleteReport(report=report.first())


class Mutation:
    create_report = CreateReport.Field()
    update_report = UpdateReport.Field()
    delete_report = DeleteReport.Field()
