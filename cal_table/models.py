from django.db import models
from datetime import datetime
# Create your models here.
class Cal_table(models.Model):
    year = datetime.today().year
    month = datetime.today().month
    day = datetime.today().day
