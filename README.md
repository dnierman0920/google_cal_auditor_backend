# Requirements: [Calendar Auditor Tool](./Avoma_Backend_Position_-_Calendar.pdf)
# Authentication: [oauth2](https://developers.google.com/identity/protocols/oauth2)


# Frontend: [google_cal_auditor_frontend](https://github.com/dnierman0920/google_cal_auditor_frontend)

# Routes

### METHOD: GET
 ```
 {{url}}/time-in-meetings/
```
#### Example JSON Response:
```JSON
{
    "Total Meeting Duration": {
        "starting_date": "2022-05-18T19:50:45.796794Z",
        "ending_date": "2022-08-18T19:50:42.356130Z",
        "days": 3,
        "hours": 13,
        "minutes": 40
    }
}
```
---
### METHOD: GET
 ```
 {{url}}/most-meetings/
```
#### Example JSON Response:
```JSON
{
    "most_and_least_meetings_per_month": {
        "most_meetings_month": {
            "year": 2018,
            "month": 7,
            "count": 24
        },
        "least_meetings_month": {
            "year": 2012,
            "month": 6,
            "count": 1
        }
    }
}
```
---
### METHOD: GET
 ```
 {{url}}/most-common-attendees/
```
#### Example JSON Response:
```JSON
{
    "most_common_attendees": {
        "dejgne@yourlekgneisba.com": 82,
        "legeeah.niegeerman@gmaegeil.com": 3,
        "niermagendaniel@gmaegeeil.com": 2
    }
}
```