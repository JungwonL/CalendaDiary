from django.db import models
from django.conf import settings
from django.contrib.auth.models import User


class Avata(models.Model):
	owner = models.ForeignKey(User, on_delete=models.CASCADE,
							  verbose_name='User', blank=True, null=True)
	image = models.FileField(upload_to="avatas",
							 null=True, blank=True, verbose_name='아바타 이미지 파일')

	def __str__(self):
		return self.owner


class UserInfo(models.Model):
	owner = models.OneToOneField(User, on_delete=models.CASCADE,
								 verbose_name='User', blank=True, null=True)
	phoneNumber = models.CharField(verbose_name='Phone', max_length=20)
	address = models.CharField(verbose_name='Address', max_length=100,
							   blank=True)
	nickname = models.CharField(verbose_name='Nick Name', max_length=12, blank=True)

	def __str__(self):
		return self.owner
