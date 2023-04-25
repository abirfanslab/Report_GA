from google.analytics.data_v1beta import BetaAnalyticsDataClient
from google.analytics.data_v1beta.types import (
    DateRange,
    Dimension,
    Metric,
    RunReportRequest,
)

def sample_run_report(property_id="357990015"):

    client = BetaAnalyticsDataClient.from_service_account_json("/Users/l.abir/Documents/fanslab/databoard/app/mod_databoard/mod_IA/AutoReports/credentials.json")

    request = RunReportRequest(
        property=f"properties/{property_id}",
        dimensions=[Dimension(name="date"), Dimension(name="language"), Dimension(name="pageTitle"), Dimension(name="deviceCategory"), Dimension(name="country"), Dimension(name="month")],
        metrics=[Metric(name="activeUsers"), Metric(name="sessions"), Metric(name="newUsers"), Metric(name="screenPageViews"), Metric(name="totalUsers"), Metric(name="engagementRate"), Metric(name="bounceRate"), Metric(name="screenPageViewsPerUser"), Metric(name="sessionsPerUser"), Metric(name="averageSessionDuration")],
        date_ranges=[DateRange(start_date="2021-12-01", end_date="today")],
    )
    response = client.run_report(request)
    return response



