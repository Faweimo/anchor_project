from django.contrib import admin
from .models import Work_log

class WorkLogsAdmin(admin.ModelAdmin):
    list_dispaly = ('first_name','department','clock_in','work_title')
    list_display_link = ('first_name','department')
    list_per_page = 25
    list_filter = ('department','clock_in')
    search_fields = ('first_name','department')


admin.site.register(Work_log,WorkLogsAdmin)