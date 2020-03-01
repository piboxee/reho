from django.urls import path

from .views import services_list, service_detail, service_create

urlpatterns = [
    path('', services_list),
    path('service_create/', service_create),
    path('<slug>/', service_detail),
]
