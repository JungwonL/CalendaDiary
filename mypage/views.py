from django.shortcuts import render
from django.views.generic import TemplateView, CreateView, UpdateView, DetailView, ListView
from django.contrib.auth.mixins import LoginRequiredMixin
from mypage.models import UserInfo
from django.urls import reverse_lazy


# # Create your views here.
# class mypage_view(TemplateView):
# 	template_name = 'mypage_index.html'
#
# def mypage_post(request):
#
# 	form = PostForm()	#PostForm클래스의 인스턴스 선언
# 	return render(request, 'mypage_form.html',{'form':form})#렌더링과 데이터전달

class mypage_view(LoginRequiredMixin, DetailView):
	template_name = 'mypage_index.html'
	model = UserInfo
	def get_object(self, queryset=None):
		UserInfo.objects.get_or_create(owner_id=self.request.user.id) #없으면 프로필 데이터 생성스
		return UserInfo.objects.get(owner_id=self.request.user.id)

	# def get_queryset(self): #이거슨 listview일 때 쓰는 것 이구요
	# 	# return UserInfo.objects.filter(owner=self.request.user)
	# 	return UserInfo.objects.get(owner=self.request.user)

class MypageFormed(LoginRequiredMixin,TemplateView):
	template_name = 'mypage_done.html'

class MyPageUV(LoginRequiredMixin,UpdateView):
	template_name = 'mypage_form.html'
	model = UserInfo
	fields = ['phoneNumber', 'address', 'nickname']


	def get_success_url(self):
		return reverse_lazy('mypage_index', kwargs={'username': self.request.user.username}) # 데이터 입력이 원활히 전송이 됐을 경우 mypage_index로 회귀

	def get_object(self, queryset=None):
		return UserInfo.objects.get(owner=self.request.user)

