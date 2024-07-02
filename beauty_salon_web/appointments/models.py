from django.db import models

from users.models import User
from salon.models import Service

#Модель для хранения и работы с датами
class DateTable(models.Model):
    date = models.DateField()

    def __str__(self):
        return str(self.date)

#Модель записей на сайте
class TimeTable(models.Model):
    FREE = 0
    OCCUPIED = 1
    STATUSES = (
        (FREE, 'Свободно'),
        (OCCUPIED, 'Занято')
    )

    date = models.ForeignKey(DateTable, on_delete=models.CASCADE)
    time_start = models.TimeField()
    time_end = models.TimeField()
    status = models.SmallIntegerField(choices=STATUSES, default=FREE)

    def __str__(self):
        return f'Дата:{self.date.date} Время: {self.time_start} - {self.time_end} | Статус: {self.status}'

#Модель скидки
class Sale(models.Model):
    name = models.CharField(max_length=256)
    percent = models.IntegerField(default=0)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

#Модель записи клиента
class Appointment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    time = models.ForeignKey(TimeTable, on_delete=models.CASCADE)
    service = models.ForeignKey(Service, on_delete=models.CASCADE)
    price = models.IntegerField(default=0, blank=True, null=True)



