# Requirements: [Calendar Auditor Tool](./Avoma_Backend_Position_-_Calendar.pdf)
# Authentication: [oauth2](https://developers.google.com/identity/protocols/oauth2)


## Frontend: TBD

## Routes
---
### METHOD: GET
 ```
 {{url}}/time-in-meetings/
```
#### Example JSON Response:
```
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