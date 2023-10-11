import random
from django.core.management.base import BaseCommand
from django.utils import timezone
from web.models import Category, Product, Order


class Command(BaseCommand):
    help = 'Заполняет базу данных тестовыми данными'

    def handle(self, *args, **options):
        self.stdout.write('Заполнение базы данных тестовыми данными...')

        # Создание категорий
        categories = ['Электроника', 'Одежда', 'Обувь', 'Аксессуары']
        for category_name in categories:
            Category.objects.create(name=category_name)

        # Создание продуктов
        for i in range(20):
            product = Product(
                name=f'Товар {i}',
                category=random.choice(Category.objects.all()),
                active=random.choice([True, False]),
                price=random.uniform(10.0, 100.0)
            )
            product.save()

        # Создание заказов
        for i in range(50):
            order = Order(
                product=random.choice(Product.objects.all()),
                order_date=timezone.now() - timezone.timedelta(days=random.randint(1, 30))
            )
            order.save()

        self.stdout.write(self.style.SUCCESS('База данных успешно заполнена тестовыми данными.'))
