from django.http import HttpResponse

def allEvents(request):
    
    return HttpResponse("This will show all Calendar Events")
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

