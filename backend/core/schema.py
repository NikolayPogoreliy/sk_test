import graphene
from graphene_django import DjangoObjectType

from backend.core.models import Account, User as UserModel


class UserType(DjangoObjectType):
    class Meta:
        model = UserModel


class AccountType(DjangoObjectType):
    class Meta:
        model = Account


class CreateAccount(graphene.Mutation):
    id = graphene.ID()
    name = graphene.String()

    class Arguments:
        id = graphene.Int()
        name = graphene.String()

    def mutate(self, info, id, name):
        account = Account.objects.create(
            id=id,
            name=name
        )
        return CreateAccount(
            id=account.id,
            name=account.name
        )


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
