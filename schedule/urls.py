from django.urls import path, re_path
from schedule.views import *

app_name = 'schedule'

urlpatterns = [
    path('schedule/<str:date>/', ScheduleDV.as_view(), name='detail'),
    # re_path(r'^schedule/?date=([\w])$', ScheduleDV.as_view(), name='detail'),

    path('<str:date>/add/', ScheduleCreateView.as_view(), name="add"),
    path('<int:pk>/update/',ScheduleUpdateView.as_view(), name="update")
]

