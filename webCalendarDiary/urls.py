"""webCalendarDiary URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.conf import settings
from django.contrib import admin
from django.conf.urls.static import static
from django.urls import path, include

<<<<<<< HEAD
from webCalendarDiary.views import *
=======

from webCalendarDiary.views import HomeView, UserCreateView, UserCreateDoneTV
>>>>>>> #5_scheduling

urlpatterns = [

	#개인정보페이지
	path('mypage/', include('mypage.urls')),

	# 로그인, 로그아웃, 비밀번호 변경 등 담당
	path('accounts/', include('django.contrib.auth.urls')),

	# 회원 가입 및 처리
	path('accounts/register/', UserCreateView.as_view(), name='register'),
<<<<<<< HEAD
	path('accounts/register/done/', UserCreateDoneTV.as_view(), name='register_done'),
=======
	path('accounts/register/done/', UserCreateDoneTV.as_view(),name='register_done'),
>>>>>>> #5_scheduling

	path('admin/', admin.site.urls),

	# 달력
	path('', HomeView.as_view(), name='home'),
<<<<<<< HEAD
	path('prev/', CalUpdateView.as_view(), name='cal'),
=======
	path('schedule/', include('schedule.urls')),

>>>>>>> #5_scheduling

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
