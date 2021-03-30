import graphene as graphene

from backend.core.schema import (CreateUser, UserQuery)
from backend.report.schema.mutations import Mutation as ReportMutation
from backend.report.schema.queries import ReportExtraQuery
from backend.template.schema.mutations import (
    ChartMutation, DimensionMutation, MetricMutation, PivotMutation,
    TemplateMutation,
)
from backend.template.schema.queries import (
    ChartQuery, DimensionQuery, MetricQuery, PivotQuery, TemplateQuery,
)
from backend.vms.schema.queries import AccountQuery, BookingQuery, VacancyQuery


class Mutation(ChartMutation, PivotMutation, MetricMutation, DimensionMutation,
    ReportMutation, TemplateMutation,
    graphene.ObjectType):
    create_user = CreateUser.Field()


class Query(UserQuery, # ReportQuery,
    ReportExtraQuery, DimensionQuery, MetricQuery, PivotQuery, ChartQuery,
    AccountQuery, BookingQuery, VacancyQuery, TemplateQuery,
    graphene.ObjectType):
    pass


# schema = graphene.Schema(query=Query, mutation=Mutation)
schema = graphene.Schema(query=Query, mutation=Mutation)
