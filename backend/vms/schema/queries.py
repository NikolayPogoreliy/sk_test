import graphene
import requests
from django.conf import settings
from graphene.types import generic
from requests.auth import HTTPBasicAuth


class AccountQuery:
    """ Get accounts list form VMS-api """
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
            start: int = 0,
            number: int = 10,
            order_predicate: str = None,
            order_direction: str = None,
            query: str = None,
            user_id: str = None
    ) -> dict:
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
            url=f"{settings.VMS_API_BASE_URL}/account/search",
            auth=HTTPBasicAuth(settings.VMS_API_LOGIN, settings.VMS_API_PASSWORD),
            json=data
        ).json()
        return response.get('data', [])


class BookingQuery:
    """ Get bookings list from VMS-api """
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
            url=f"{settings.VMS_API_BASE_URL}/booking/search",
            auth=HTTPBasicAuth(settings.VMS_API_LOGIN, settings.VMS_API_PASSWORD),
            json=data
        ).json()
        return response.get('data', [])


class VacancyQuery:
    """ Get vacancies list from VMS-api"""
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
            url=f"{settings.VMS_API_BASE_URL}/vacancy/search",
            auth=HTTPBasicAuth(settings.VMS_API_LOGIN, settings.VMS_API_PASSWORD),
            json=data
        ).json()
        return response.get('data', [])
