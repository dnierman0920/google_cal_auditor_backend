from django.http import HttpResponse
import datetime
from .toolbox.datesAndTimes import event_duration, events_per_month, most_and_least_meetings_per_month
from rest_framework import status
from .authenticate import authenitcate
from dateutil.relativedelta import relativedelta
from django.http import JsonResponse 

nowDatetime = datetime.datetime.utcnow().isoformat() + 'Z'  # 'Z' indicates UTC time

def pastMonths(monthsAgo: int):
    # Subtract 20 months from a given datetime object
    return datetime.datetime.now() - relativedelta(months=monthsAgo) 

service  = authenitcate()

def allEvents(request):

        # Call the Calendar API
        events_result = service.events().list(calendarId='primary',
                                              singleEvents=True,
                                              orderBy='startTime').execute()
        events = events_result.get('items', [])

        if not events:
            print('No upcoming events found.')
            return HttpResponse("There are no calemdar events to display")

        # Prints the start and name of the next 10 events
        return JsonResponse({'AllEvents': events }, status=status.HTTP_201_CREATED)

# This will show Total time spent in meetings per month for the last 3 months
def timeInMeetings(request):
        # variables to return in response
        totalMeetingDuration = datetime.timedelta(days=0, seconds=0, microseconds=0, milliseconds=0, minutes=0, hours=0, weeks=0) # total time in meetings
        print("totalMeetingDuration Starting Point: ", totalMeetingDuration)
        todayDate = nowDatetime
        threeMonthsAgoDate = pastMonths(3).isoformat() + 'Z' 

        # Call the Calendar API
        events_result = service.events().list(calendarId='primary',
                                              singleEvents=True,
                                              timeMax = todayDate,
                                              timeMin = threeMonthsAgoDate,
                                              orderBy='startTime').execute()
        events = events_result.get('items', [])
        for event in events:
            duration = event_duration(event)
            if duration:   # sometimes duration returns None for all day events
                totalMeetingDuration += duration
            days, hours, minutes = totalMeetingDuration.days, totalMeetingDuration.seconds // 3600, totalMeetingDuration.seconds // 60 % 60
        return JsonResponse({'total_meeting_duration':
                        {
                            "starting_date": threeMonthsAgoDate,
                            "ending_date": todayDate,
                            "days": days,
                            "hours": hours,
                            "minutes": minutes
                        } }, status=status.HTTP_200_OK)

def mostMeetings(request):
    todayDate = nowDatetime

    # Call the Calendar API
    events_result = service.events().list(calendarId='primary',
                                            singleEvents=True,
                                            timeMax = todayDate,
                                            orderBy='startTime').execute()
    events = events_result.get('items', [])
    most_least_meetings_by_month = most_and_least_meetings_per_month(events_per_month(events))

    return JsonResponse({"most_and_least_meetings_per_month":
                most_least_meetings_by_month}
                 , status=status.HTTP_200_OK)
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

