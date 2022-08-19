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

def most_and_least_meetings_per_month(events_count: dict):
    # this will hold the key value of the year and month
    most_meetings_month = {}
    least_meetings_month = {}

    most_meetings = None
    least_meetings = None

    years = events_count.keys()

    for year in years:
        for month in events_count[year].keys():
            # set the starting values
            if most_meetings == None: most_meetings = events_count[year][month] 
            if least_meetings == None: least_meetings = events_count[year][month]

            # find most meetings
            if events_count[year][month] > most_meetings:
                most_meetings = events_count[year][month]
                most_meetings_month = {} # remove the old value to replace with new below
                most_meetings_month[str(year) + ", " + str(month)] = most_meetings

            # find least meetings
            if events_count[year][month] < least_meetings:
                least_meetings = events_count[year][month]
                least_meetings_month = {} # remove the old value to replace with new below
                print("year type: ", type(year))
                print("month type: ", type(month))
                least_meetings_month[str(year) + ", " + str(month)] = least_meetings

    print("most_meetings_month: ", most_meetings_month )
    print("least_meetings_month: ", least_meetings_month )


        



        
