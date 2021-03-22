import requests

api_url = 'https://staging.stellen-anzeiger.ch/admin/api'


def get_accounts(user_id=None, ):
    response = requests.post(url=api_url, )
