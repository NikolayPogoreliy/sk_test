import datetime

# import matplotlib.pyplot as plt
# import numpy as np
from apiclient.discovery import build
from django.conf import settings
from django.db.models import QuerySet
from oauth2client.service_account import ServiceAccountCredentials

# Fixing random state for reproducibility
from backend.template.models import Pivot, Template

# np.random.seed(19680801)

SCOPES = ['https://www.googleapis.com/auth/analytics.readonly']
KEY_FILE_LOCATION = settings.KEY_FILE_LOCATION
VIEW_ID = '70495155'


def initialize_analyticsreporting():
    """Initializes an Analytics Reporting API V4 service object.

    Returns:
    An authorized Analytics Reporting API V4 service object.
    """
    credentials = ServiceAccountCredentials.from_json_keyfile_name(
        KEY_FILE_LOCATION, SCOPES)

    # Build the service object.
    analytics = build('analyticsreporting', 'v4', credentials=credentials)

    return analytics


def get_pivot_request(pivots: QuerySet[Pivot] = None) -> dict:
    """
    Form pivot dict for GA request
    :param pivots: queryset with Pivot instances
    :return: dict with pivot parameters
    """
    if not pivots:
        return {}
    pivot_list = [
        {
            "dimensions": [
                {'name': dim.name} for dim in pivot.dimensions.all()
            ],
            "metrics": [
                {"expression": metr.name} for metr in pivot.metrics.all()
            ],
            "maxGroupCount": pivot.max_group_count,
            "startGroup": pivot.start_group
        } for pivot in pivots
    ]
    # print(pivot_list)
    return {'pivots': pivot_list}


def get_report(analytics, report_querysets: list) -> dict:
    """Queries the Analytics Reporting API V4.

    Args:
    analytics: An authorized Analytics Reporting API V4 service object.
    Returns:
    The Analytics Reporting API V4 response.
    """
    if not report_querysets:
        report_querysets = [
            {
                'viewId': VIEW_ID,
                'dateRanges': [{'startDate': '7daysAgo', 'endDate': 'today'}],
                'metrics': [{'expression': 'ga:sessions'}],
                'dimensions': [{'name': 'ga:country'}]
            }
        ]
    return analytics.reports().batchGet(
        body={
            'reportRequests': report_querysets
        }
    ).execute()


def get_analytics(template_id: str, date_from: datetime.date, date_to: datetime.date) -> dict:
    """ Send request to GA-api and get response with GA-analytics"""
    analytics = initialize_analyticsreporting()
    target = Template.objects.get(id=template_id)
    report_querysets = []
    chart_names = []
    for chart in target.charts.all():
        chart_dict = {
            'viewId': target.ga_view_id,
            'dateRanges': [{
                'startDate': date_from.isoformat(),
                'endDate': date_to.isoformat()
            }],
            'metrics': [{'expression': metric.name} for metric in chart.metrics.all()],
            'dimensions': [{'name': dimension.name} for dimension in chart.dimensions.all()]
        }
        pivots = get_pivot_request(chart.pivots.all())
        if pivots:
            chart_dict.update(pivots)
        if target.filter_expression:
            chart_dict.update({'filtersExpression': target.filter_expression})
        report_querysets.append(chart_dict)
        chart_names.append(chart.name)
    response = get_report(analytics, report_querysets)
    response.update({'charts': chart_names})
    return response
