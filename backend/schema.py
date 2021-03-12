import graphene as graphene

from backend.core.models import Account, User as UserModel
from backend.core.schema import (AccountType, CreateAccount, CreateUser, UserType)


class Query(graphene.ObjectType):
    users = graphene.List(UserType)
    user = graphene.Field(UserType, id=graphene.Int())

    accounts = graphene.List(AccountType)
    account = graphene.Field(AccountType, id=graphene.Int())

    def resolve_users(self, info, **kwargs):
        return UserModel.objects.all()

    def resolve_accounts(self, info, **kwargs):
        return Account.objects.all()

    def resolve_user(self, info, **kwargs):
        if 'id' in kwargs:
            return UserModel.objects.filter(id=id).first()
        return UserModel.objects.none()

    def resolve_account(self, info, **kwargs):
        if 'id' in kwargs:
            return Account.objects.filter(id=id).first()
        return Account.objects.none()


class Mutation(graphene.ObjectType):
    create_user = CreateUser.Field()
    create_account = CreateAccount.Field()


# schema = graphene.Schema(query=Query, mutation=Mutation)
schema = graphene.Schema(query=Query, mutation=Mutation)