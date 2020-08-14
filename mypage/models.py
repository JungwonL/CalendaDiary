from django.db import models
from django.contrib.auth.models import User




class Avata(models.Model):
	owner = models.ForeignKey(User, on_delete=models.CASCADE,
							  verbose_name='User', blank=True, null=True)
	image = models.FileField(upload_to="avatas",
							 null=True, blank=True, verbose_name='아바타 이미지 파일')

	def __str__(self):
		return self.owner
