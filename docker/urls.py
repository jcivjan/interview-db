from django.urls import path, re_path, include
from django.contrib import admin

urlpatterns = [
    path('admin/', admin.site.urls),
    re_path(r'^', include('interview_db.urls')),
]
