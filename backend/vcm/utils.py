import base64
import io
from datetime import timedelta

import matplotlib.pyplot as plt
import numpy as np
from apiclient.discovery import build
from django.conf import settings
from django.db.models import QuerySet
from django.utils.timezone import now
from oauth2client.service_account import ServiceAccountCredentials

# Fixing random state for reproducibility
np.random.seed(19680801)

from target.models import Pivot

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
    # print(pivots)
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


def fig_to_base64(fig):
    img = io.BytesIO()
    fig.savefig(img, format='png',
                bbox_inches='tight')
    img.seek(0)

    return base64.b64encode(img.getvalue())


def print_response(response):
    """Parses and prints the Analytics Reporting API V4 response.

    Args:
      response: An Analytics Reporting API V4 response.
    """
    result = []
    for report in response.get('reports', []):
        columnHeader = report.get('columnHeader', {})
        dimensionHeaders = columnHeader.get('dimensions', [])
        metricHeaders = columnHeader.get('metricHeader', {}).get('metricHeaderEntries', [])

        x_values = [': '.join(row.get('dimensions')) for row in report.get('data', {}).get('rows', [])]
        y_values_raw = [[int(element) for element in row.get('metrics', {})[0].get('values')] for row in
                        report.get('data', {}).get('rows', [])]
        y_values = np.array(y_values_raw).transpose().tolist()
        N = len(x_values)

        ind = np.arange(N)  # the x locations for the groups
        width = 0.35  # the width of the bars: can also be len(x) sequence
        fig, ax = plt.subplots()
        p = [plt.bar(ind, y_values[0], width)]
        for i in range(1, len(y_values)):
            p.append(
                plt.bar(ind, y_values[i], width, bottom=y_values[i - 1])
            )
        for i in range(len(x_values)):
            plt.annotate(x_values[i], (ind[i], 0.1), rotation=90)

        # plt.title('Scores by group and gender')
        x_ticks, x_legend = [], []
        for pos, val in enumerate(x_values, 1):
            x_ticks.append(f'p{pos}')
            x_legend.append(f'p{pos}: {val}')
        plt.xticks(ind, x_ticks, rotation=90, rotation_mode='anchor')
        y_max = sum([int(s) for s in report.get('data', {}).get('maximums', {})[0].get('values', [])])
        plt.yticks(np.arange(0, y_max + 1))
        plt.legend((p_h[0] for p_h in p), (m.get('name') for m in metricHeaders))
        # fig.savefig('tmp.png', bbox_inches='tight')
        result.append(fig_to_base64(fig))
    return result


def get_analytics(target_id):
    analytics = initialize_analyticsreporting()
    target = Target.objects.get(id=target_id)
    report_querysets = []
    chart_names = []
    for chart in target.chart.all():
        chart_dict = {
            'viewId': target.ga_view_id,
            'dateRanges': [{
                'startDate': (now() - timedelta(days=30)).date().isoformat(),
                'endDate': 'today'
            }],
            'metrics': [{'expression': metric.name} for metric in chart.metrics.all()],
            'dimensions': [{'name': dimension.name} for dimension in chart.dimensions.all()]
        }
        pivots = get_pivot_request(chart.pivot.all())
        if pivots:
            chart_dict.update(pivots)
        if target.filter:
            chart_dict.update({'filtersExpression': target.filter})
        report_querysets.append(chart_dict)
        chart_names.append(chart.name)
    response = get_report(analytics, report_querysets)
    response.update({'charts': chart_names})
    return response
