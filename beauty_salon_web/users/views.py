from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.contrib import messages, auth
from django.urls import reverse
from django.contrib.auth.decorators import login_required

from users.forms import UserLoginForm, UserRegistrationForm, UserProfileForm
from appointments.models import Appointment, Sale

#Авторизация
def login(request):
    if request.method == 'POST':
        form = UserLoginForm(data=request.POST)
        if form.is_valid():
            username = request.POST['username']
            password = request.POST['password']
            user = auth.authenticate(username=username, password=password)
            if user:
                auth.login(request, user)
                return HttpResponseRedirect(reverse('index'))
    else:
        form = UserLoginForm()
    context = {
        'title': 'Авторизация',
        'form': form,
    }
    return render(request, 'users/login.html', context)

#Регистрация
def registration(request):
    if request.method == 'POST':
        form = UserRegistrationForm(data=request.POST)
        if form.is_valid():
            user = form.save()

            sale = Sale()
            sale.name = 'Скидка на первый заказ 20%'
            sale.user = user
            sale.percent = 20
            sale.save()

            messages.success(request, 'Регистрация прошла успешно!')
            return HttpResponseRedirect(reverse('users:login'))
    else:
        form = UserRegistrationForm
    context = {
        'title': 'Регистрация',
        'form': form,
    }
    return render(request,'users/registration.html', context)

#Просмотр профиля
@login_required
def profile(request):
    if request.method == 'POST':
        form = UserProfileForm(instance=request.user, data=request.POST, files=request.FILES)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('users:profile'))
    else:
        form = UserProfileForm(instance=request.user)

    context = {
        'title': 'Профиль',
        'form': form,
        'appointment': Appointment.objects.filter(user=request.user),
        'sales': Sale.objects.filter(user=request.user),
    }
    return render(request, 'users/profile.html', context)

#Выход из профиля
def logout(request):
    auth.logout(request)
    return HttpResponseRedirect(reverse('index'))

#Панель администратора
def admin_panel(request):
    context = {
        'title': 'Панель администратора'
    }
    return render(request, 'users/admin-panel.html', context)

