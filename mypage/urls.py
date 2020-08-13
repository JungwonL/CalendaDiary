from webCalendarDiary.views import *
from django.urls import path, include

urlpatterns = [
	path('avata/<int:pk>/add/', AvataView.as_view(), name='avata_add'),
	path('avata/<int:id>', avata_view, name='avata'),
]