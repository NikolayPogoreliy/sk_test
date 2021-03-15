import graphene as graphene

from backend.core.schema import (CreateUser, UserQuery)
from backend.report.schema import ReportQuery


class Mutation(graphene.ObjectType):
    create_user = CreateUser.Field()


class Query(UserQuery, ReportQuery, graphene.ObjectType):
    pass


# schema = graphene.Schema(query=Query, mutation=Mutation)
schema = graphene.Schema(query=Query, mutation=Mutation)
