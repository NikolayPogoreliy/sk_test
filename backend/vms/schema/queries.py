import requests
from graphene.types import generic
from requests.auth import HTTPBasicAuth


class AccountsQuery:
    vmsaccounts = generic.GenericScalar(
        # generic.GenericScalar,
        # start=graphene.Int(required=True, default_value=0),
        # number=graphene.Int(required=True, default_value=10),
        # order_predicate=graphene.String(required=False),
        # order_direction=graphene.String(required=False),
        # query=graphene.String(required=False),
        # user_id=graphene.String(required=False)
    )

    def resolve_vmsaccounts(
            self, info,
            # start=0,
            # number=10,
            # order_predicate=None,
            # order_direction=None,
            # query=None,
            # user_id=None
    ):
        data = dict(start=0, number=10)
        # if order_predicate:
        #     data['oder_predicate'] = order_predicate
        # if order_direction:
        #     data['oder_direction'] = order_direction
        # if query:
        #     data['query'] = query
        # if user_id:
        #     data['user_id'] = user_id
        response = requests.post(
            url="https://staging.stellen-anzeiger.ch/admin/api/account/search",
            auth=HTTPBasicAuth('analytics', 'analytics'),
            json=data
        ).json()
        return response.get('data', [])
        # return {"adr": "awe"}
