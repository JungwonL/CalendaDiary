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
		return UserInfo.objects.get(owner=self.request.user)

	# def get_queryset(self): #이거슨 listview일 때 쓰는 것 이구요
	# 	# return UserInfo.objects.filter(owner=self.request.user)
	# 	return UserInfo.objects.get(owner=self.request.user)

class MypageFormed(LoginRequiredMixin,TemplateView):
	template_name = 'mypage_done.html'

class MyPageCV(CreateView):
	template_name = 'mypage_form.html'
	model = UserInfo
	fields = ['phoneNumber', 'address', 'nickname']
	success_url = reverse_lazy('mypage_done')  # 데이터 입력이 원활히 전송이 됐을 경우 mypage_index로 회귀

	def form_valid(self, form):  # 유효성 검사
		form.instance.owner = self.request.user  # user는 field데이터에서 구성되어있지 않으므로 사용자 권한 전달
		try: #기존 데이터가 있으면 삭제
			userinfo = UserInfo.objects.get(owner_id=self.request.user.id)
			userinfo.delete()
		except:
			pass
		return super().form_valid(form)  # 데이터 베이스로 넘기는 과정

class MyPageUV(LoginRequiredMixin,UpdateView):
	template_name = 'mypage_form.html'
	model = UserInfo
	fields = ['phoneNumber', 'address', 'nickname']
	success_url = reverse_lazy('mypage_done')  # 데이터 입력이 원활히 전송이 됐을 경우 mypage_index로 회귀

	def get_object(self, queryset=None):
		return UserInfo.objects.get(owner=self.request.user)