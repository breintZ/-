from django.urls import path

from users.views import login, registration, profile, logout, admin_panel

app_name = 'users'

urlpatterns = [
    path('login/', login, name='login'),
    path('registration/', registration, name='registration'),
    path('profile/', profile, name='profile'),
    path('logout/', logout, name='logout'),
    path('admin_panel/', admin_panel, name='admin_panel'),
]