from django.shortcuts import render
from django.views.generic import TemplateView
# Create your views here.
class mypage_view(TemplateView):
	template_name = 'mypage_index.html'