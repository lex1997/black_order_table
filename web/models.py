from datetime import timedelta

from django.db import models
from django.utils import timezone


class Category(models.Model):
    name = models.CharField(max_length=100, verbose_name="Название категории")

    def __str__(self):
        return self.name


class Product(models.Model):
    name = models.CharField(max_length=255, verbose_name="Название товара")
    category = models.ForeignKey(Category, on_delete=models.CASCADE, verbose_name="Категория")
    active = models.BooleanField(default=True, verbose_name="Статус активности")
    price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="Цена")
    created_at = models.DateTimeField(default=timezone.now, verbose_name="Дата создания")

    def __str__(self):
        return self.name

    @property
    def orders_last_month(self):
        today = timezone.now()
        last_month_start = (today.replace(day=1, hour=0, minute=0, second=0, microsecond=0) - timedelta(days=1)).replace(day=1)
        last_month_end = today.replace(day=1, hour=0, minute=0, second=0, microsecond=0) - timedelta(days=1)
        orders = self.order_set.filter(order_date__range=[last_month_start, last_month_end])
        return orders.count()

    @property
    def orders_current_month(self):
        today = timezone.now()
        current_month_start = today.replace(day=1, hour=0, minute=0, second=0, microsecond=0)
        orders = self.order_set.filter(order_date__gte=current_month_start)
        return orders.count()


class Order(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, verbose_name="Товар")
    order_date = models.DateTimeField(default=timezone.now, verbose_name="Дата заказа")

    def __str__(self):
        return f"Заказ товара '{self.product.name}' от {self.order_date}"
