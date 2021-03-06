from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static



urlpatterns = [
    path('logs/',include('worklogs.urls')),
    path('staff/',include('staff.urls')),
    path('',include('accounts.urls')),
    path('admin/', admin.site.urls),
] + static(settings.STATIC_URL,document_root=settings.STATIC_ROOT)
