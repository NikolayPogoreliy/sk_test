import graphene
from graphene_django import DjangoObjectType

from backend.core.models import User as UserModel, Account


class UserType(DjangoObjectType):
    class Meta:
        model = UserModel


class AccountType(DjangoObjectType):
    class Meta:
        model = Account


class CreateAccount(graphene.Mutation):
    id = graphene.Int()
    acc_id = graphene.Int()
    name = graphene.String()

    class Arguments:
        acc_id = graphene.Int()
        name = graphene.String()

    def mutate(self, info, acc_id, name):
        account = Account.objects.create(
            acc_id=acc_id,
            name=name
        )
        return CreateAccount(
            id=account.id,
            acc_id=account.acc_id,
            name=account.name
        )


class CreateUser(graphene.Mutation):
    id = graphene.Int()
    first_name = graphene.String()
    last_name = graphene.String()
    email = graphene.String()

    class Arguments:
        first_name = graphene.String()
        last_name = graphene.String()
        email = graphene.String()

    @classmethod
    def mutate(cls, root, info, first_name, last_name, email):
        user = UserModel(first_name=first_name, last_name=last_name, email=email)
        user.save()

        return CreateUser(
            id=user.id,
            first_name=user.first_name,
            last_name=user.last_name,
        )


class UserQuery(graphene.ObjectType):
    users = graphene.List(UserType)

    def resolve_users(self, info):
        return UserModel.objects.all()


class AccountQuery(graphene.ObjectType):
    account = graphene.List(AccountType)

    def resolve_account(self, info, **kwargs):
        if 'name' in kwargs:
            return Account.objects.filter(name__contains=kwargs.get('name'))
        return Account.objects.all()


class UserMutation(graphene.ObjectType):
    create_user = CreateUser.Field()


class AccountMutation(graphene.ObjectType):
    create_user = CreateAccount.Field()
