from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('pages/', include('pages.urls')),  # include -> 포워딩해버려
    path('utils/', include('utils.urls')),
]
