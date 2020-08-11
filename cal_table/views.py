from django.shortcuts import render
from django.views.generic import ListView, DetailView
from cal_table.models import Cal_table
from django.views.generic.dates import TodayArchiveView

# Create your views here.
class HomeView(ListView):
    model = Cal_table
    # date_field = 'modify_dt'
