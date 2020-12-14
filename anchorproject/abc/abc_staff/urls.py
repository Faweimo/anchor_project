from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static



urlpatterns = [
    path('logs/',include('logs.urls')),
    path('',include('staff.urls')),
    path('admin/', admin.site.urls),
] + static(settings.STATIC_URL,document_root=settings.STATIC_ROOT)
