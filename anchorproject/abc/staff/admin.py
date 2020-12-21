from django.contrib import admin
from .models import *

# Register your models here.

class StaffAdmin(admin.ModelAdmin):
    list_display = ('staff_id','user','department')
    list_display_link = ('staff_id','user')
    search_fields = ('staff_id','user')
    list_filter = ('department',)
    list_per_page = 25

admin.site.register(StaffProfile,StaffAdmin)
