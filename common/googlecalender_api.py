from __future__ import print_function
import httplib2
import os

from apiclient import discovery
from oauth2client import client
from oauth2client import tools
from oauth2client.file import Storage

from datetime import date

try:
    import argparse
    flags = tools.argparser.parse_args([])
except ImportError:
    flags = None

# If modifying these scopes, delete your previously saved credentials
# at ~/.credentials/calendar-python-quickstart.json
SCOPES = 'https://www.googleapis.com/auth/calendar.readonly'
CLIENT_SECRET_FILE = 'secret/client_secret_304978972420-331511h3leqhkneeaft4pklqsgr8qjsp.apps.googleusercontent.com.json'
APPLICATION_NAME = 'Google Calendar API Python Quickstart'


def _get_credentials():
    """Gets valid user credentials from storage.

    If nothing has been stored, or if the stored credentials are invalid,
    the OAuth2 flow is completed to obtain the new credentials.

    Returns:
        Credentials, the obtained credential.
    """
    home_dir = os.path.expanduser('~')
    credential_dir = os.path.join(home_dir, '.credentials')
    if not os.path.exists(credential_dir):
        os.makedirs(credential_dir)
    credential_path = os.path.join(credential_dir,
                                   'calendar-python-quickstart.json')

    store = Storage(credential_path)
    credentials = store.get()
    if not credentials or credentials.invalid:
        flow = client.flow_from_clientsecrets(CLIENT_SECRET_FILE, SCOPES)
        flow.user_agent = APPLICATION_NAME
        if flags:
            credentials = tools.run_flow(flow, store, flags)
        else: 
            credentials = tools.run(flow, store)
        print('Storing credentials to ' + credential_path)
    return credentials

def get_holiday_events(year):
    """Shows basic usage of the Google Calendar API.

    Creates a Google Calendar API service object and outputs a list of the next
    10 events on the user's calendar.
    """
    credentials = _get_credentials()
    http = credentials.authorize(httplib2.Http())
    service = discovery.build('calendar', 'v3', http=http)

    calendar_id = 'ja.japanese#holiday@group.v.calendar.google.com'
    calendar_min = date(year=year, month=1, day=1).isoformat() + 'T00:00:00.000000Z'
    calendar_max = date(year=year, month=12, day=31).isoformat() + 'T00:00:00.000000Z'

    event_results = service.events().list(
      calendarId = calendar_id,
      timeMin = calendar_min,
      timeMax = calendar_max,
      maxResults = 50,
      singleEvents = True,
      orderBy = "startTime"
    ).execute()

    events = event_results.get('items', [])
    
    return events