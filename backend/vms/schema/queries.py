import graphene
import requests
from graphene.types import generic
from requests.auth import HTTPBasicAuth


class AccountQuery:
    vms_accounts = generic.GenericScalar(
        start=graphene.Int(required=True, default_value=0),
        number=graphene.Int(required=True, default_value=10),
        order_predicate=graphene.String(required=False),
        order_direction=graphene.String(required=False),
        query=graphene.String(required=False),
        user_id=graphene.String(required=False)
    )

    def resolve_vms_accounts(
            self, info,
            start=0,
            number=10,
            order_predicate=None,
            order_direction=None,
            query=None,
            user_id=None
    ):
        data = dict(start=start, number=number)
        if order_predicate:
            data['oderPredicate'] = order_predicate
        if order_direction:
            data['oderDirection'] = order_direction
        if query:
            data['query'] = query
        if user_id:
            data['userId'] = user_id
        response = requests.post(
            url="https://staging.stellen-anzeiger.ch/admin/api/account/search",
            auth=HTTPBasicAuth('analytics', 'analytics'),
            json=data
        ).json()
        return response.get('data', [])


class BookingQuery:
    vms_bookings = generic.GenericScalar(
        start=graphene.Int(required=True, default_value=0),
        number=graphene.Int(required=True, default_value=10),
        order_predicate=graphene.String(required=False),
        order_direction=graphene.String(required=False),
        query=graphene.String(required=False),
        account_id=graphene.String(required=False)
    )

    def resolve_vms_bookings(
            self, info,
            start=0,
            number=10,
            order_predicate=None,
            order_direction=None,
            query=None,
            account_id=None
    ):
        data = dict(start=start, number=number)
        if order_predicate:
            data['oderPredicate'] = order_predicate
        if order_direction:
            data['oderDirection'] = order_direction
        if query:
            data['query'] = query
        if account_id:
            data['accountId'] = account_id
        response = requests.post(
            url="https://staging.stellen-anzeiger.ch/admin/api/booking/search",
            auth=HTTPBasicAuth('analytics', 'analytics'),
            json=data
        ).json()
        return response.get('data', [])


class VacancyQuery:
    vms_vacancies = generic.GenericScalar(
        start=graphene.Int(required=True, default_value=0),
        number=graphene.Int(required=True, default_value=10),
        order_predicate=graphene.String(required=False),
        order_direction=graphene.String(required=False),
        query=graphene.String(required=False),
        account_id=graphene.String(required=False),
        booking_id=graphene.String(required=False)
    )

    def resolve_vms_vacancies(
            self, info,
            start=0,
            number=10,
            order_predicate=None,
            order_direction=None,
            query=None,
            booking_id=None,
            account_id=None
    ):
        data = dict(start=start, number=number)
        if order_predicate:
            data['oderPredicate'] = order_predicate
        if order_direction:
            data['oderDirection'] = order_direction
        if query:
            data['query'] = query
        if account_id:
            data['accountId'] = account_id
        if booking_id:
            data['bookingId'] = booking_id
        response = requests.post(
            url="https://staging.stellen-anzeiger.ch/admin/api/vacancy/search",
            auth=HTTPBasicAuth('analytics', 'analytics'),
            json=data
        ).json()
        return response.get('data', [])
