import logging

from graphene_django_extras import (
    DjangoListObjectField,
)

from backend.report.schema.types import (
    ReportListType,
)

logger = logging.getLogger(__name__)


class ReportExtraQuery:
    reports = DjangoListObjectField(ReportListType,
        description='All Reports query')
    # report = DjangoObjectField(
    #     ReportListType,
    #     description='Single User query'
    # )
    report = ReportListType.RetrieveField(description='Single User query')
