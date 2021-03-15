import graphene as graphene
from graphene_django import DjangoObjectType

from backend.core.models import User as UserModel


class UserType(DjangoObjectType):
    class Meta:
        model = UserModel


class CreateUser(graphene.Mutation):
    id = graphene.Int()
    first_name = graphene.String()
    last_name = graphene.String()
    email = graphene.String()
    username = graphene.String()

    class Arguments:
        first_name = graphene.String()
        last_name = graphene.String()
        email = graphene.String()
        username = graphene.String()

    @classmethod
    def mutate(cls, root, info, first_name, last_name, email, username):
        user = UserModel(first_name=first_name, last_name=last_name, email=email, username=username)
        user.save()

        return CreateUser(
            id=user.id,
            first_name=user.first_name,
            last_name=user.last_name,
            username=user.username
        )


class UserQuery:
    users = graphene.List(UserType)
    user = graphene.Field(UserType, user_id=graphene.ID())

    def resolve_users(self, info, **kwargs):
        return UserModel.objects.all()

    def resolve_user(self, info, user_id):
        return UserModel.objects.get(id=user_id)
