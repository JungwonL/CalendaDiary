from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView, UpdateView
from schedule.models import Schedule
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from django.utils import timezone
import datetime


class ScheduleLV(ListView):
    model = Schedule
    context_object_name = 'schedule_list'


class ScheduleDV(LoginRequiredMixin, DetailView):
    model = Schedule
    context_object_name = 'schedule'

    def get_object(self):
        date = self.kwargs["date"]

        schedule_date = datetime.datetime.strptime(date, '%Y-%m-%d')  # url에서 날짜 받아오기
        schedules = Schedule.objects.filter(schedule_date__date=schedule_date, is_temporary_schedule=False)
        Schedule.objects.get_or_create(schedule_date=schedule_date, user_id_fk=self.request.user, is_temporary_schedule=True)
        context = {}  # html에서 사용할 변수들 추가
        context['date'] = date
        print(date)
        context['schedule_date'] = schedule_date
        context['schedules'] = schedules
        return context


class ScheduleGlobalCreateView(LoginRequiredMixin, CreateView):
    model = Schedule
    context_object_name = 'schedule'
    fields = ['schedule_date', 'title', 'description']

    def form_valid(self, form):
        form.instance.user_id_fk = self.request.user
        return super().form_valid(form)

    def get_success_url(self):
        dateAndhour = self.object.schedule_date
        date = dateAndhour.date()
        return reverse_lazy('schedule:detail', kwargs={'date': date})



class ScheduleCreateView(LoginRequiredMixin,UpdateView):
    model = Schedule
    context_object_name = 'schedule'
    fields = ['schedule_date', 'title', 'description']

    def get_object(self):
        date = self.kwargs["date"]
        schedule_date = datetime.datetime.strptime(date, '%Y-%m-%d')
        return Schedule.objects.get(schedule_date=schedule_date, user_id_fk=self.request.user,
                                       is_temporary_schedule=True)
    def form_valid(self, form):
        form.instance.is_temporary_schedule = False
        return super().form_valid(form)

    def get_success_url(self):
        dateAndhour = self.object.schedule_date
        date = dateAndhour.date()
        return reverse_lazy('schedule:detail', kwargs={'date': date})
