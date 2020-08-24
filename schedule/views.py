from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView
from schedule.models import Schedule
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from django.utils import timezone
import datetime


class ScheduleLV(ListView):
    model = Schedule
    context_object_name = 'schedule_list'


class ScheduleDV(DetailView):
    model = Schedule
    context_object_name = 'schedule'

    def get_object(self):
        date = self.kwargs["date"]
        schedule_date = datetime.datetime.strptime(date, '%Y-%m-%d')  # url에서 날짜 받아오기
        schedules = Schedule.objects.filter(schedule_date__date=schedule_date)

        context = {}  # html에서 사용할 변수들 추가
        context['schedule_date'] = schedule_date
        context['schedules'] = schedules
        print(schedules)
        return context


class ScheduleCreateView(LoginRequiredMixin, CreateView):
    model = Schedule
    context_object_name = 'schedule'

    fields = ['schedule_date', 'title', 'description']
    success_url = reverse_lazy('schedule:detail')

