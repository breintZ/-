from django.urls import path

from appointments.views import (date_and_time, appointments_create, appointments, appointments_delete,
                                appointment_sale, date_and_time_edit, date_and_time_delete, date_delete, sale_add)

app_name = 'appointments'

urlpatterns = [
    path('date_and_time/<int:service_id>', date_and_time, name='date_and_time'),
    path('appointments_create/<int:time_id>/<int:service_id>', appointments_create, name='appointments_create'),
    path('appointments_create_sale/<int:time_id>/<int:service_id>/<int:sale_id>', appointments_create, name='appointments_create_sale'),
    path('appointments/<int:time_id>/<int:service_id>', appointments, name='appointments'),
    path('appointments_sale/<int:time_id>/<int:service_id>/<int:sale_id>', appointment_sale, name='appointments_sale'),
    path('appointments_delete/<int:app_id>', appointments_delete, name='appointments_delete'),
    path('date_and_time_edit/', date_and_time_edit, name='date_and_time_edit'),
    path('date_and_time_delete/<int:time_id>', date_and_time_delete, name='date_and_time_delete'),
    path('date_delete/<int:date_id>', date_delete, name='date_delete'),
    path('sale_add/', sale_add, name='sale_add'),
]