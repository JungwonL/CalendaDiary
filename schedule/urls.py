from django.urls import path, re_path
from schedule.views import *

app_name = 'schedule'

urlpatterns = [
    path('', ScheduleLV.as_view(), name='index'),
    path('schedule/', ScheduleLV.as_view(), name='index'),
    path('schedule/<str:date>/', ScheduleDV.as_view(), name='detail'),
    # re_path(r'^schedule/?date=([\w])$', ScheduleDV.as_view(), name='detail'),

    path('<str:date>/add/', ScheduleCreateView.as_view(), name="add"),
]

