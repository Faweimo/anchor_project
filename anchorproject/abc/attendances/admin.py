from django.contrib import admin
from .models import Attendance

class AttendanceAdmin(admin.ModelAdmin):
    list_display = ('name','department','team-leader')
    list_per_page = 25
    search_fields = ('name','department')
    list_display_link = ('name','department')
    list_filter = ('department',)

admin.site.register(Attendance)
