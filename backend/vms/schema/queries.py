import graphene


class AccountsQuery:
    args = graphene.JSONString()

    def resolve_args(self, info):
        # return requests.post(
        #     url="https://staging.stellen-anzeiger.ch/admin/api/vacancy/search",
        #     auth=HTTPBasicAuth('analytics', 'analytics')
        # ).json()
        return {"adr": "awe"}
