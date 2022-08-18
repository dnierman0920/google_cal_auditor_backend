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

