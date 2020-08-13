from django.contrib import admin

# Register your models here.
from cal_table.models import Cal_table

@admin.register(Cal_table)
class Cal_table_admin(admin.ModelAdmin):
    pass