from django.db import models
from django.contrib.auth.models import User
from tinymce.models import HTMLField
from twilio.rest import Client

# Create your models here.

class Schedule(models.Model):
    schedule_date = models.DateTimeField()
    title = models.CharField(max_length=50)
    description = models.CharField(max_length=50, blank=True, null=True)
    national_holiday_fk = models.IntegerField(null=True)
    content = HTMLField('CONTENT', null=True)
    user_id_fk = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, db_column='user_id_fk')

    class Meta:
        db_table = 'schedules'
        ordering = ('-schedule_date',)

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        account_sid = 'AC598feaeef0ecd3f0508c56e8944c01e4'
        auth_token = 'e9d9591701607c8308eafdfb2d647076'
        client = Client(account_sid, auth_token)

        message = client.messages.create(
            body=f'Hello from Calda. Your schedule is {self.title} on {self.schedule_date}',
            from_='+13342922554',
            to='+821093690964'
        )

        print(message.sid)
        return super().save(*args, **kwargs)