import datetime

from django.contrib.auth.models import User
from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver


# Create your models here.
class Jeweller(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, verbose_name='Користувач')
    PIB = models.CharField(max_length=90, null=False, blank=False, verbose_name='ПІБ')

    def __str__(self):
        return f"{self.PIB}"


class Order(models.Model):
    delivery_choices = [
        ('yes', 'Так'),
        ('no', 'Ні')
    ]
    broadcast_choices = [
        ('yes', 'Так'),
        ('no', 'Ні')
    ]
    PIB = models.CharField(max_length=90, null=False, blank=False, verbose_name='ПІБ')
    phone_number = models.CharField(max_length=45, null=False, blank=False, verbose_name='Номер телефону')
    address = models.CharField(max_length=90, null=False, blank=False, verbose_name='Адреса')
    fk_jeweller = models.ForeignKey(Jeweller, on_delete=models.CASCADE, verbose_name='Ювелір', blank=True, null=True)
    type_of_jewellery = models.CharField(max_length=45, null=False, blank=False, verbose_name='Замовлення')
    delivery = models.CharField(max_length=3, choices=delivery_choices, null=False, blank=False,
                                verbose_name='Доставка')
    broadcast = models.CharField(max_length=3, choices=broadcast_choices, null=False, blank=False,
                                 verbose_name='Трансляція')
    discount = models.PositiveIntegerField(null=True, blank=True, verbose_name='Знижка')
    order_datetime = models.DateTimeField(null=False, blank=False, default=datetime.datetime.now())

    def __str__(self):
        return f"Номер замовлення: {self.id}, ПІБ: {self.PIB}, Тип: {self.type_of_jewellery}"


class CompletedProduct(models.Model):
    state_choices = [
        ('preparing', 'Підготовка'),
        ('in_process', 'В процесі'),
        ('complete', 'Готово'),
    ]
    name = models.CharField(max_length=45, null=False, blank=False, verbose_name='Назва')
    amount = models.PositiveIntegerField(verbose_name='Кількість')
    size = models.CharField(max_length=45, null=False, blank=False, verbose_name='Розмір')
    price = models.PositiveIntegerField(verbose_name='Ціна')
    state = models.CharField(max_length=10, choices=state_choices, null=False, blank=False, verbose_name='Стан')
    image = models.ImageField(verbose_name='Зображення', default='default.jpg')
    order = models.ForeignKey(Order, null=True, blank=True, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.name}, {self.state}"


class UsedMaterials(models.Model):
    type = models.CharField(max_length=45, null=False, blank=False, verbose_name='Тип')
    name = models.CharField(max_length=45, null=False, blank=False, verbose_name='Назва')
    amount = models.PositiveIntegerField(verbose_name='Кількість')
    fk_completed_product = models.ForeignKey(CompletedProduct, on_delete=models.CASCADE, verbose_name='Готовий товар')

    def __str__(self):
        return f"{self.name}, {self.amount}"
