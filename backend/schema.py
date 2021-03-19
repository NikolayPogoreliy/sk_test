import graphene as graphene

from backend.core.schema import (CreateUser, UserQuery)
from backend.report.schema import Mutation as ReportMutation, ReportQuery
from backend.template.schema.mutations import ChartMutation
from backend.template.schema.queries import DimensionQuery


class Mutation(ChartMutation, ReportMutation, graphene.ObjectType):
    create_user = CreateUser.Field()


class Query(
    UserQuery,
    ReportQuery,
    DimensionQuery,
    graphene.ObjectType):
    pass


# schema = graphene.Schema(query=Query, mutation=Mutation)
schema = graphene.Schema(query=Query, mutation=Mutation)
