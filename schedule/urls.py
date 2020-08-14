from django.urls import path, re_path
from django.contrib import admin
from schedule.views import *

app_name = 'schedule'

urlpatterns = [
    path('', ScheduleLV.as_view(), name='index'),
    re_path(r'^schedule/(?P<schedulde_date>[-\w]+)/$', ScheduleDV.as_view(), name='detail'),
    path('add/', ScheduleCreateView.as_view(), name="add"),
    # path('', ScheduleDV.as_view(), name='detail'),
]