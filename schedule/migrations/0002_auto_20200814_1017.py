# Generated by Django 3.1 on 2020-08-14 10:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('schedule', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='schedule',
            name='national_holiday_fk',
            field=models.IntegerField(null=True),
        ),
    ]
