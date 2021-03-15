import graphene as graphene

from backend.core.models import User as UserModel
from backend.core.schema import (CreateUser, UserType)


class Query(graphene.ObjectType):
    users = graphene.List(UserType)
    user = graphene.Field(UserType, id=graphene.Int())

    def resolve_users(self, info, **kwargs):
        return UserModel.objects.all()

    def resolve_user(self, info, **kwargs):
        if 'id' in kwargs:
            return UserModel.objects.filter(id=id).first()
        return UserModel.objects.none()


class Mutation(graphene.ObjectType):
    create_user = CreateUser.Field()


# schema = graphene.Schema(query=Query, mutation=Mutation)
schema = graphene.Schema(query=Query, mutation=Mutation)