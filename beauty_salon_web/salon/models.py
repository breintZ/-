from django.db import models


class Category(models.Model): #Модель категорий услуг
    name = models.CharField(max_length=256)

    def __str__(self):
        return self.name

#Модель услуг
class Service(models.Model):
    name = models.CharField(max_length=256)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    price = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f'{self.name} | Категория: {self.category.name}'

