from django.http import HttpResponse
import datetime
from .toolbox.datesAndTimes import event_duration, events_per_month, most_and_least_meetings_per_month, rank_attendees_by_meetings
from rest_framework import status
from .authenticate import authenitcate
from dateutil.relativedelta import relativedelta
from django.http import JsonResponse 

#  CLEAN THIS UP TO FIND A BETTER PLACE FOR IT?
def pastMonths(monthsAgo: int):
    # Subtract 20 months from a given datetime object
    return datetime.datetime.now() - relativedelta(months=monthsAgo) 

# vars repeated in multiple requests
nowDatetime = datetime.datetime.utcnow().isoformat() + 'Z'  # 'Z' indicates UTC time
todayDate = nowDatetime
threeMonthsAgoDate = pastMonths(3).isoformat() + 'Z' 


service  = authenitcate()

#**************************************************************************************************
#                               ALL EVENTS (FOR TESTING    
#**************************************************************************************************

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

#**************************************************************************************************
#                               TOTAL TIME SPENT IN MEETINGS    
#**************************************************************************************************

def timeInMeetings(request):
        # variables to return in response
        totalMeetingDuration = datetime.timedelta(days=0, seconds=0, microseconds=0, milliseconds=0, minutes=0, hours=0, weeks=0) # total time in meetings

        # Call the Calendar API
        events_result = service.events().list(calendarId='primary',
                                              singleEvents=True,
                                              timeMax = todayDate,
                                              timeMin = threeMonthsAgoDate,
                                              orderBy='startTime').execute()
        events = events_result.get('items', [])

        # ****** CLEAN THIS UP BY PUTTING THE FOR LOOP BEFORE INTO DURATION FUNCITON IN TOOL ****

        # loop through events, pull start and end time, calculate duration
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

#**************************************************************************************************
#                               MONTHS WITH MOST AND LEAST MEETINGS   
#**************************************************************************************************

def mostMeetings(request):
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

#**************************************************************************************************
#                                   MOST COMMON ATTENDEES   
#**************************************************************************************************                 

def mostCommonAttendees(request):
        # Call the Calendar API
    events_result = service.events().list(calendarId='primary',
                                            singleEvents=True,
                                            timeMin = threeMonthsAgoDate,
                                            orderBy='startTime').execute()
    events = events_result.get('items', [])
    top_three_attendees = rank_attendees_by_meetings(events)
    return JsonResponse({"most_common_attendees":
            top_three_attendees}
                , status=status.HTTP_200_OK)

#**************************************************************************************************
#                                   BELOW IS WORK IN PROGRESS  
#**************************************************************************************************   

# def busiestWeek(request):
#     return HttpResponse("This will show Busiest week - you can select a threshold of your choice")
# def relaxedWeek(request):
#     return HttpResponse("This will show Relaxed week week - you can select a threshold of your choice")
# def averageNumberOfMeetings(request):
#     return HttpResponse("This will show The average number of meetings per week")
# def averageTimeInMeetings(request):
#     return HttpResponse("This will show The average time spent every week in meetings")
# def timeSpentInterviewing(request):
#     return HttpResponse("This will show Time spent in Recruiting/Conducting interviews")

