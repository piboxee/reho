from django.urls import path

from .views import (services_list,
                    service_detail,
                    service_create,
                    service_update,
                    service_delete,
                    )

urlpatterns = [
    path('', services_list),
    path('service_create/', service_create),
    path('<slug>/', service_detail),
    path('<slug>/service_update/', service_update),
    path('<slug>/service_delete/', service_delete)
]
