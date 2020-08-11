from django.db import models

# Create your models here.
class Cal_table(models.Model):
    y = models.IntegerField('year')
    m = models.IntegerField('month')
