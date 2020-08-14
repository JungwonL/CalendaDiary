from django.shortcuts import render
from django.views.generic import ListView, DetailView
from schedule.models import Schedule
from django.urls import reverse_lazy

# Create your views here.

class ScheduleLV(ListView):
    model = Schedule
    context_object_name = 'schedule_list'

class ScheduleDV(DetailView):
    model = Schedule
    context_object_name = 'schedule'