from django.contrib import admin
from .models import Category, Product, Order

# Определение verbose_name и verbose_name_plural для моделей
Category._meta.verbose_name = "Категория"
Category._meta.verbose_name_plural = "Категории"

Product._meta.verbose_name = "Товар"
Product._meta.verbose_name_plural = "Товары"

Order._meta.verbose_name = "Заказ"
Order._meta.verbose_name_plural = "Заказы"


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name',)
    list_per_page = 25


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'category', 'active', 'price', 'created_at')
    list_filter = ('category', 'active')
    search_fields = ('name', 'category__name')
    list_per_page = 25


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ('product', 'order_date')
    list_filter = ('order_date',)
    search_fields = ('product__name', 'order_date')
    list_per_page = 25
