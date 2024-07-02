from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.contrib.auth.decorators import login_required

from salon.models import Category, Service
from salon.forms import ServiceForm

#Отображение главное страницы
def index(request):
    context = {
        'title': 'Главная'
    }
    return render(request, 'salon/index.html', context)

#Отображение страницы с услугами, фильтруя их по категории,
#если передан соответствующий идентификатор категории.
def service(request, category_id=None):
    if category_id:
        category = Category.objects.get(id=category_id)
        services = Service.objects.filter(category=category)
    else:
        services = Service.objects.all()

    context = {
        'title': 'Услуги',
        'services': services,
        'categoty': Category.objects.all()
    }
    return render(request, 'salon/service.html', context)


#Добавление товара (услуги) администротором
@login_required
def service_add(request):
    if request.method == 'POST':
        form = ServiceForm(data=request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
    else:
        form = ServiceForm()

    context = {
        'title': 'Добавить товар',
        'form': form,
    }
    return render(request, 'salon/service-add.html', context)


#Удаление товара (услуги) администратором
@login_required
def service_delete(request, service_id=None):
    service = Service.objects.get(id=service_id)
    service.delete()
    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))

