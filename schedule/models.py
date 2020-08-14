from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Schedule(models.Model):
    schedule_date = models.DateTimeField()
    title = models.CharField(max_length=50)
    description = models.CharField(max_length=50, blank=True, null=True)
    national_holiday_fk = models.IntegerField(null=True)
    user_id_fk = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, db_column='user_id_fk')

    class Meta:
        db_table = 'schedules'
        ordering = ('-schedule_date',)

    def __str__(self):
        return self.title
