from django.urls import path

from salon.views import service_add, service_delete

app_name = 'salon'

urlpatterns = [
    path('service_add', service_add, name='service_add'),
    path('service_delete/<int:service_id>', service_delete, name='service_delete'),
]
