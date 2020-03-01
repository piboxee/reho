from django.contrib import admin
from django.urls import path, include

from services.views import services_list

urlpatterns = [
    path('services/', include('services.urls')),

    path('admin/', admin.site.urls),
]
