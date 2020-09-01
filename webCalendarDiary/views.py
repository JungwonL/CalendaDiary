from django.views.generic import TemplateView, CreateView,ListView
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from mypage.models import *
from webCalendarDiary import settings
from django.http import HttpResponse
from schedule.models import *
import os
import json

# TemplateView
class HomeView(ListView):
	model = Schedule
	context_object_name = 'schedule_list'
	template_name = 'home.html'

	def get_context_data(self, **kwargs):
		context = super().get_context_data(**kwargs)
		schedules = Schedule.objects.filter(user_id_fk=self.request.user.id)
		context['schedule_list'] = schedules
		return context

class Home2View(ListView):
	model = Schedule
	context_object_name = 'Schedule_list'
	template_name = 'home2.html'



class CalUpdateView(TemplateView):
	template_name = 'home_cal_update.html'


	def get_context_data(self, **kwargs):
		context = super().get_context_data(**kwargs)
		schedules = Schedule.objects.filter(user_id_fk=self.request.user.id)
		context['schedule_list'] = schedules
		return context

# --- User Creation
class UserCreateView(CreateView):
	template_name = 'registration/register.html'
	form_class = UserCreationForm
	success_url = reverse_lazy('register_done')


class UserCreateDoneTV(TemplateView):
	template_name = 'registration/register_done.html'

# -- Avata Creation
class AvataView(LoginRequiredMixin, CreateView):
	model = Avata
	fields = ['image']
	template_name = "registration/avata_form.html"
	success_url = reverse_lazy('home')

	def form_valid(self, form):
		form.instance.owner = self.request.user
		try:  # 기존 아바타가 있으면 삭제
			avata = Avata.objects.get(owner_id=self.request.user.id)
			file_path = os.path.join(settings.MEDIA_ROOT, str(avata.image))
			os.remove(file_path)
			avata.delete()
		except:
			pass

		return super().form_valid(form)  # Post 모델 저장, self.object


def avata_view(request, id):
	try:
		avata = Avata.objects.get(owner_id=id)
		file_path = os.path.join(settings.MEDIA_ROOT, str(avata.image))
	except:  # 등록된 아바타가 없는 경우 디폴트 아바타 이미지 사용
		file_path = os.path.join(settings.MEDIA_ROOT, 'avatas/avata.jpg')
	return HttpResponse(open(file_path, 'rb'), content_type="image/*")

