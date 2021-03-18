import graphene as graphene

from backend.core.schema import (CreateUser, UserQuery)
from backend.report.schema import ReportQuery, Mutation as ReportMutation
from backend.template.schema import DimensionQuery


class Mutation(ReportMutation, graphene.ObjectType):
    create_user = CreateUser.Field()


class Query(
    UserQuery,
    ReportQuery,
    DimensionQuery,
    graphene.ObjectType):
    pass


# schema = graphene.Schema(query=Query, mutation=Mutation)
schema = graphene.Schema(query=Query, mutation=Mutation)
