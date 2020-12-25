from django.contrib import admin

# Register your models here.
from .models import *


@admin.register(Staff)
class StaffAdmin(admin.ModelAdmin):
    list_display=['staff_id','staff_name','contact_number','designation','salary','joining_date']