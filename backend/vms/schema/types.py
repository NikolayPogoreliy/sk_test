import graphene


class BaseVmsType(graphene.ObjectType):
    start = graphene.Int()
    number = graphene.Int()
    order_predicate = graphene.String()
    ordef_direction = graphene.String()
    query = graphene.String()

    # def get_


class VmsAccountType(BaseVmsType):
    user_id = graphene.Int()


class VmsBookingType(BaseVmsType):
    account_id = graphene.Int()


class VmsVacaniyType(BaseVmsType):
    account_id = graphene.Int()
    booking_id = graphene.Int()
