from django.contrib import admin
from .models import Logger



class LogAdmin(admin.ModelAdmin):
    list_display = ('work_id','full_name','email','department')
    list_display_link = ('user_id','work_id','full_name','email')
    search_fields = ('full_name','team_leader','department')
    list_filter = ('full_name','team_leader','department')
    list_per_page = 25

admin.site.register(Logger,LogAdmin)
