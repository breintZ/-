from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings

from salon.views import index, service

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index, name='index'),
    path('service/', service, name='service'),
    path('category/<int:category_id>', service, name='category'),
    path('users/', include('users.urls', namespace='users')),
    path('appointments/', include('appointments.urls', namespace='appointments')),
    path('salon/', include('salon.urls', namespace='salon')),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)