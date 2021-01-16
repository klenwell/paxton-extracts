from datetime import date, timedelta
import csv
from config.secrets import CLIENT_ID, SECRET_ID
from services.business_activity_service import BusinessActivityService


#
# Main Method
#
def main():
    service = BusinessActivityService(CLIENT_ID, SECRET_ID)
    activities = service.fetch_activities()
    csv_path = write_to_csv(activities)
    print('Wrote {} activities to {}'.format(len(activities), csv_path))


def write_to_csv(activities):
    csv_path = 'o365-activites-{}.csv'.format(date.today().strftime('%Y%m%d'))
    csv_header = [
        'Date',
        'Type',
        'Start',
        'End',
        'Time',
        'Duration',
        'Title',
        'Client',
        'Owner',
        'Description',
        'Categories'
    ]

    with open(csv_path, 'w', newline='') as f:
        writer = csv.writer(f)
        writer.writerow(csv_header)

        for activity in activities:
            writer.writerow(activity.to_csv())

    return csv_path


#
# Test / Sandbox Methods
#
def test_csv():
    """Like main but extends start date to pull in more data if testing with
    infrequently used account with sparse data set.
    """
    start_date = date(2020, 11, 1)
    end_date = date.today()
    service = BusinessActivityService(CLIENT_ID, SECRET_ID)
    activities = service.fetch_activities(start_date, end_date)
    csv_path = write_to_csv(activities)
    print('Wrote {} activities to {}'.format(len(activities), csv_path))


def activities():
    start_date = date(2020, 11, 1)
    end_date = date.today()
    service = BusinessActivityService(CLIENT_ID, SECRET_ID)
    activities = service.fetch_activities(start_date, end_date)
    print(len(activities))
    breakpoint()


def api_data():
    service = BusinessActivityService(CLIENT_ID, SECRET_ID)
    end = date.today()
    start = end - timedelta(days=28)

    emails = service.fetch_emails(start, end)
    meetings = service.fetch_meetings(start, end)
    breakpoint()


#
# Main Block
#
main()
