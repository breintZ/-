from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from django.contrib.auth.decorators import login_required

from appointments.models import Appointment, DateTable, TimeTable, Sale
from salon.models import Service
from appointments.forms import DateForm, TimeForm, SaleForm

#Отображение страницы выбора даты и времени для записи на услугу
@login_required
def date_and_time(request, service_id):
    time = TimeTable.objects.all()
    date = DateTable.objects.all()
    service = Service.objects.get(id=service_id)

    context = {
        'time': time,
        'title': 'Выбор времени',
        'date': date,
        'service': service,
    }
    return render(request, 'appointments/date-and-time.html', context)

#Отображение страницы редактирования расписания, где пользователь
#может добавлять и редактировать даты и времена записей на услугу.
@login_required
def date_and_time_edit(request):
    time = TimeTable.objects.all()
    date = DateTable.objects.all()

    if request.method == 'POST':
        form_date = DateForm(data=request.POST, files=request.FILES)
        if form_date.is_valid():
            form_date.save()
            return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
    else:
        form_date = DateForm()

    if request.method == 'POST':
        form_time = TimeForm(data=request.POST, files=request.FILES)
        if form_time.is_valid():
            form_time.save()
            return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
    else:
        form_time = TimeForm()

    context = {
        'time': time,
        'title': 'Редактор раписания',
        'date': date,
        'form_date': form_date,
        'form_time': form_time
    }
    return render(request, 'appointments/date-and-time-edit.html', context)

#Удаление времени и даты записи из расписания
@login_required
def date_and_time_delete(request, time_id):
    time = TimeTable.objects.get(id=time_id)
    time.delete()

    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))


def date_delete(request, date_id):
    date = DateTable.objects.get(id=date_id)
    date.delete()

    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))

#Запись на услугу
@login_required
def appointments(request, time_id, service_id):
    time = TimeTable.objects.get(id=time_id)
    service = Service.objects.get(id=service_id)
    sales = Sale.objects.filter(user=request.user)

    context = {
        'time': time,
        'service': service,
        'title': 'Запись',
        'sales': sales,
    }
    return render(request, 'appointments/appointment.html', context)

#Запись на услугу с применением скидки
@login_required
def appointment_sale(request, time_id, service_id, sale_id):
    time = TimeTable.objects.get(id=time_id)
    service = Service.objects.get(id=service_id)

    sale = Sale.objects.get(id=sale_id)
    sale_percent = sale.percent
    service_price = service.price
    price = int(service_price) - sale_percent / 100 * int(service_price)

    context = {
        'time': time,
        'service': service,
        'title': 'Запись',
        'price': price,
        'sale': sale,
    }
    return render(request, 'appointments/appointments_sale.html', context)

#Создание записи администратором
@login_required
def appointments_create(request, time_id, service_id, sale_id=None):
    time = TimeTable.objects.get(id=time_id)
    service = Service.objects.get(id=service_id)

    appointment = Appointment()
    appointment.time = time
    appointment.service = service
    appointment.user = request.user

    if sale_id:
        sale = Sale.objects.get(id=sale_id)
        sale_percent = sale.percent
        service_price = service.price
        price = int(service_price) - sale_percent / 100 * int(service_price)
        appointment.price = price
        appointment.save()
        sale.delete()
    else:
        appointment.price = service.price
        appointment.save()

    time.status = 1
    time.save()

    return HttpResponseRedirect(reverse('users:profile'))

#Удаление записи администратором
@login_required
def appointments_delete(request, app_id):
    appointment = Appointment.objects.get(id=app_id)
    time = TimeTable.objects.get(id=appointment.time.id)
    time.status = 0
    time.save()

    appointment.delete()
    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))

#Добавление скидки администратором
def sale_add(request):
    if request.method == 'POST':
        form = SaleForm(data=request.POST, files=request.FILES)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
    else:
        form = SaleForm()

    sales = Sale.objects.all()

    context = {
        'title': 'Скидки',
        'sales': sales,
        'form': form
    }
    return render(request, 'appointments/sale_add.html', context)
