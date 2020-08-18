from django.shortcuts import render
from django.views.generic import TemplateView, CreateView, UpdateView
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

class mypage_view(TemplateView):
	template_name = 'mypage_index.html'


class MyPageCV(CreateView):
	template_name = 'mypage_form.html'
	model = UserInfo
	fields = ['phoneNumber', 'address', 'nickname']
	success_url = reverse_lazy('mypage_index')  # 데이터 입력이 원활히 전송이 됐을 경우 mypage_index로 회귀

	def form_valid(self, form):  # 유효성 검사
		form.instance.owner = self.request.user  # user는 field데이터에서 구성되어있지 않으므로 사용자 권한 전달
		return super().form_valid(form)  # 데이터 베이스로 넘기는 과정


class MyPageUV(UpdateView):
	template_name = 'mypage_form.html'
	model = UserInfo
	fields = ['phoneNumber', 'address', 'nickname']
	success_url = reverse_lazy('mypage_index')  # 데이터 입력이 원활히 전송이 됐을 경우 mypage_index로 회귀

	def form_valid(self, form):
		form.instance.owner = self.request.user
		return super().form_valid(form)  # 데이터베이스로 넘기는 과정
