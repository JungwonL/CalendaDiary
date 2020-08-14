from webCalendarDiary.views import *
from mypage.views import mypage_view
from django.urls import path, include

urlpatterns = [
	path('avata/<int:pk>/add/', AvataView.as_view(), name='avata_add'),
	path('avata/<int:id>', avata_view, name='avata'),
	path('',mypage_view.as_view(), name ='mypage_index')
]