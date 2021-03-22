import requests
from graphene.types import generic
from requests.auth import HTTPBasicAuth


class AccountsQuery:
    args = generic.GenericScalar()

    def resolve_args(self, info):
        response = requests.post(
            url="https://staging.stellen-anzeiger.ch/admin/api/vacancy/search",
            auth=HTTPBasicAuth('analytics', 'analytics'),
            json={'start': 0, 'number': 1}
        ).json()
        return response.get('data', [])
        # return {"adr": "awe"}
