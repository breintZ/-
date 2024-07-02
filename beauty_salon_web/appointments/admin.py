from django.contrib import admin

from appointments.models import Appointment, DateTable, TimeTable, Sale

admin.site.register(Appointment)
admin.site.register(DateTable)
admin.site.register(TimeTable)
admin.site.register(Sale)

