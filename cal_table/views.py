from django.shortcuts import render

from django.views.generic import ListView, DetailView
from cal_table.models import Cal_table

# Create your views here.
class HomeView(ListView):
    model = Cal_table
