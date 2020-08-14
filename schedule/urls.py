from django.urls import path
from django.contrib import admin
from schedule.views import *

app_name = 'schedule'

urlpatterns = [
    path('', ScheduleLV.as_view(), name='index'),
    # path('', ScheduleDV.as_view(), name='detail'),
]