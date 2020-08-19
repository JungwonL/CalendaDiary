from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView
from schedule.models import Schedule
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from django.utils import timezone

# Create your views here.

class ScheduleLV(ListView):
    model = Schedule
    context_object_name = 'schedule_list'

    def get_queryset(self):     # Schedule.objects.all()
        date = self.kwargs["date"]
        return super().get_queryset().filter(schedule_date )

    # def get_context_data(self, **kwargs):
    #     pass
    #
    #     # context = super().get_context_data(**kwargs)
    #     # context["date"] = date
    #     # schedule = self.get_object()
    #     # schedule.save()
    #     # return context


class ScheduleDV(DetailView):
    model = Schedule
    context_object_name = 'schedule'

    def get_object(self):
        date = self.kwargs["date"]
        print(date)
        return ""
        # return Schedule.objects.get(schedule_date = date)



class ScheduleCreateView(LoginRequiredMixin, CreateView):
    model = Schedule

    fields = ['schedule_date', 'title', 'description']
    success_url = reverse_lazy('blog:index')

    def form_valid(self, form):
        form.instance.owner = self.request.user
        form.instance.modify_dt = timezone.now()

        response = super().form_valid(form) #post모델 저장, self.object

        files = self.request.FILES.getlist("files")
        for file in files:
            # attach_file = PostAttachFile(post=self.object, filename=file.name, size=file.size, content_type=file.content_type, upload_file=file)
            attach_file.save()
        return response
