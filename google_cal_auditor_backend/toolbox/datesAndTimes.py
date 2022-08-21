from datetime import datetime
import iso8601 # for date string -> date object

def event_duration(event):
    """This function takes an event and returns its duration (if it is NOT an all day event)"""

    # parse the event to pull start and end time
    start = event['start'].get('dateTime')
    end = event['end'].get('dateTime')

    #if it is an all day event return 0
    if start == None or end == None:
        return None

    #convert string date into date object
    startTime = iso8601.parse_date(start)
    endTime = iso8601.parse_date(end)
    duration = endTime - startTime
    return duration

def events_per_month(events):
    """this function returns a dictionary that organizes meeting(event) counts per year and month"""

    # Organize the dates by year and then by month
    # create an empty dictionary to store the counts
    events_count ={}

    for event in events:
        # print("event: ", event)
        # parse the event to pull start and end time
        start = event['start'].get('dateTime')
        #if it is an all day event return 0
        if start == None:
            continue
        start_date_object = iso8601.parse_date(event['start'].get('dateTime'))
        # information about datetime can be found here: https://docs.python.org/3/library/datetime.html
        date  = start_date_object.date()
        year = start_date_object.year
        month = start_date_object.month
        
        # print(f'sorting an event with year {year} and month {month}')
        # check to see if the dictionary key for the year exists 
        if year in events_count:
            events_count[year][month] += 1
        else:
            # create a dictionary 1-12
            months = {}
            for i in range(1,13):
                months[i] = 0
            events_count[year] = months
            # add one count
            events_count[year][month] += 1

    # print("Events Count: ", events_count)
    return(events_count)

# !!! COME BACK TO THIS AND REEVALUATE HOW TO DEAL WITH MONTHS THAT HAVE SAME NUMBER OF MEETINGS !!!
def most_and_least_meetings_per_month(events_count: dict):
    """this function returns a dictionary that has the 'year, month' as the key and number of meetings
     that month as the value - for the months with the most and least meetings""" 
    # this will hold the key value of the year and month
    most_meetings_month = None
    least_meetings_month = None

    most_meetings = None
    least_meetings = None

    years = events_count.keys()

    for year in years:
        for month in events_count[year].keys():
            # set the starting values
            if most_meetings == None: most_meetings = events_count[year][month] 
            if least_meetings == None:
                if events_count[year][month] > 0:
                    least_meetings = events_count[year][month]

            # find most meetings
            if events_count[year][month] > most_meetings:
                most_meetings = events_count[year][month]
                most_meetings_month = {
                                        "year":year,
                                        "month":month,
                                        "count": most_meetings,
                                    }

            # find least meetings (not including months with zero meetings)
            if least_meetings and events_count[year][month] > 0 and events_count[year][month] < least_meetings: # need to check if least meetings is not None to proceed
                least_meetings = events_count[year][month]
                least_meetings_month = {
                                        "year":year,
                                        "month":month,
                                        "count": least_meetings
                                    }

    # print("most_meetings_month: ", most_meetings_month )
    # print("least_meetings_month: ", least_meetings_month )

    return(
        {
        "most_meetings_month": most_meetings_month,
        "least_meetings_month": least_meetings_month
        }
    )

def rank_attendees_by_meetings(events):
    """This function will show how many meetings you have had with each attendee"""

    # attendee_count dictionary will store 'attendee: meeting(event) count'
    attendee_count = {}

    # loop through each event and pull the attendee list
    for event in events:
        # if the attendees list is zero skip the iteration and go on to next event ****
        if not "attendees" in event: 
            continue
        # loop through each attendee list to pull the attendees
        for attendee in event["attendees"]:
            if not "email" in attendee: # found some attendees without display names..(accounting for it here -> come back to with alterantive solution --> changed it to email for now)
                continue
            else:
                email = attendee["email"]
                if email in attendee_count:
                    attendee_count[email] += 1
                # if the attendees name is not in the dictionary add with value = 1
                elif "self" not in attendee: # self only appears as a key if it is true
                    # print("new attendee: ", attendee)
                    attendee_count[email] = 1

    # print("attendee_count: ", attendee_count)

    # sort the list from greatest to least
    sorted_attendee_count = sorted(attendee_count.items(), key=lambda x: x[1], reverse=True)
    # print("sorted_attendee_count: ", sorted_attendee_count)

    #return top three most common attendees
    top_three_attendees = {}

    i = 0
    for key, value in sorted_attendee_count:
        if i < 3:
            top_three_attendees[key] = value
            i += 1 
        else:
            break
    # print("top_three_attendees", top_three_attendees)

    return(top_three_attendees)


