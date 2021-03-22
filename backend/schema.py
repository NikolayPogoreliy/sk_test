import graphene as graphene

from backend.core.schema import (CreateUser, UserQuery)
from backend.report.schema import Mutation as ReportMutation, ReportQuery
from backend.template.schema.mutations import ChartMutation, DimensionMutation, MetricMutation, PivotMutation
from backend.template.schema.queries import ChartQuery, DimensionQuery, MetricQuery, PivotQuery
from backend.vms.schema.queries import AccountQuery, BookingQuery, VacancyQuery


class Mutation(
    ChartMutation,
    PivotMutation,
    MetricMutation,
    DimensionMutation,
    ReportMutation,
    graphene.ObjectType):
    create_user = CreateUser.Field()


class Query(
    UserQuery,
    ReportQuery,
    DimensionQuery,
    MetricQuery,
    PivotQuery,
    ChartQuery,
    AccountQuery,
    BookingQuery,
    VacancyQuery,
    graphene.ObjectType):
    pass


# schema = graphene.Schema(query=Query, mutation=Mutation)
schema = graphene.Schema(query=Query, mutation=Mutation)
