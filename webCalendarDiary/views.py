from django.views.generic import TemplateView, CreateView
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy

from schedule.views import ScheduleLV

# TemplateView
class HomeView(ScheduleLV):
	template_name = 'home.html'


# --- User Creation
class UserCreateView(CreateView):
	template_name = 'registration/register.html'
	form_class = UserCreationForm
	success_url = reverse_lazy('register_done')


class UserCreateDoneTV(TemplateView):
	template_name = 'registration/register_done.html'

