from webCalendarDiary.views import *
from mypage.views import *
from django.urls import path, include

urlpatterns = [
	path('avata/<int:pk>/add/', AvataView.as_view(), name='avata_add'),
	path('avata/<int:id>', avata_view, name='avata'),
	path('profile/<str:username>', mypage_view.as_view(), name='mypage_index'),
	path('update', MyPageUV.as_view(), name='mypage_update'),
	path('formed', MypageFormed.as_view(), name='mypage_done')
]
