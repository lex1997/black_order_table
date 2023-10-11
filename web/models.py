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


class Order(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, verbose_name="Товар")
    order_date = models.DateTimeField(default=timezone.now, verbose_name="Дата заказа")

    def __str__(self):
        return f"Заказ товара '{self.product.name}' от {self.order_date}"

    @classmethod
    def orders_last_month(cls):
        last_month = timezone.now() - timezone.timedelta(days=30)
        return cls.objects.filter(order_date__gte=last_month).count()

    @classmethod
    def orders_current_month(cls):
        current_month = timezone.now().replace(day=1, hour=0, minute=0, second=0, microsecond=0)
        return cls.objects.filter(order_date__gte=current_month).count()
