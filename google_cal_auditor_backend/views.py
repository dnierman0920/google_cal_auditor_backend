from django.http import HttpResponse
import datetime
import os.path
from pprint import pprint
from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError

# If modifying these scopes, delete the file token.json.
SCOPES = ['https://www.googleapis.com/auth/calendar.readonly']

def allEvents(request):
    """Shows basic usage of the Google Calendar API.
    Prints the start and name of the next 10 events on the user's calendar.
    """
    creds = None
    # The file token.json stores the user's access and refresh tokens, and is
    # created automatically when the authorization flow completes for the first
    # time.
    if os.path.exists('token.json'):
        creds = Credentials.from_authorized_user_file('token.json', SCOPES)
    # If there are no (valid) credentials available, let the user log in.
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file(
                'credentials.json', SCOPES)
            creds = flow.run_local_server(port=0)
        # Save the credentials for the next run
        with open('token.json', 'w') as token:
            token.write(creds.to_json())

    try:
        service = build('calendar', 'v3', credentials=creds)

        # Call the Calendar API
        now = datetime.datetime.utcnow().isoformat() + 'Z'  # 'Z' indicates UTC time
        print('Getting the upcoming 10 events')
        events_result = service.events().list(calendarId='primary', timeMin=now,
                                              maxResults=1, singleEvents=True,
                                              orderBy='startTime').execute()
        events = events_result.get('items', [])
        pprint(events)


        if not events:
            print('No upcoming events found.')
            return

        # Prints the start and name of the next 10 events
        for event in events:
            start = event['start'].get('dateTime', event['start'].get('date'))
            print(start, event['summary'])

    except HttpError as error:
        print('An error occurred: %s' % error)
    return HttpResponse(events)
def timeInMeetings(request):
    return HttpResponse("This will show Total time spent in meetings per month for the last 3 months")
def mostMeetings(request):
    return HttpResponse("This will show Which month had the highest number of meetings / least number of meetings")
def busiestWeek(request):
    return HttpResponse("This will show Busiest week - you can select a threshold of your choice")
def relaxedWeek(request):
    return HttpResponse("This will show Relaxed week week - you can select a threshold of your choice")
def averageNumberOfMeetings(request):
    return HttpResponse("This will show The average number of meetings per week")
def averageTimeInMeetings(request):
    return HttpResponse("This will show The average time spent every week in meetings")
def mostCommonAttendees(request):
    return HttpResponse("This will show Top 3 persons with whom you have meetings")
def timeSpentInterviewing(request):
    return HttpResponse("This will show Time spent in Recruiting/Conducting interviews")

