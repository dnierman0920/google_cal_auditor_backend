"""google_cal_auditor_backend URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path("admin/", admin.site.urls),
    # 1. Total time spent in meetings per month for the last 3 months
    path("time-in-meetings/", views.timeInMeetings, name='time-in-meetings'),
    # 2. Which month had the highest number of meetings / least number of meetings
    path("most-meetings/", admin.site.urls),
    # 3. Busiest week / relaxed week - you can select a threshold of your choice
    path("busiest-week/", admin.site.urls),
    path("relaxed-week/", admin.site.urls),
    # 4. The average number of meetings per week, average time spent every week in
    # meetings.
    path("average-number-of-meetings/", admin.site.urls),
    path("average-time-in-meetings/", admin.site.urls),
    # 5. Top 3 persons with whom you have meetings
    path("most-common-atendees/", admin.site.urls),
    # 6. Time spent in Recruiting/Conducting interviews
    path("time-spent-interviewing/", admin.site.urls),
]
