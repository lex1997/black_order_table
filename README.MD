# Проект "black_order" 

## Описание
Проект "black_order" представляет собой веб-приложение, разработанное с использованием Django 4.2.6. Это приложение позволяет отслеживать информацию о продуктах, их категориях и связанных заказах. Проект также включает интеграцию с Bootstrap для оформления страниц.

## Установка

Для разворачивания проекта необходимо выполнить следующие шаги:

1. Установите Python и Poetry, если они еще не установлены:
   ```bash
   pip install poetry
   ```

2. Клонируйте репозиторий "black_order":
   ```bash
   git clone https://github.com/yourusername/black_order.git
   cd black_order
   ```

3. Создайте виртуальное окружение и установите зависимости:
   ```bash
   poetry install
   ```

4. Примените миграции:
   ```bash
   python manage.py migrate
   ```

5. Запустите приложение:
   ```bash
   python manage.py runserver
   ```

## Доступные методы

Проект "black_order" включает следующие доступные методы:

1. **Просмотр таблицы с данными:**
   - URL: /table/
   - Описание: Позволяет просматривать информацию о продуктах, включая их ID, название, категорию, статус активности, цену, количество заказов за прошлый месяц и текущий месяц.
   - Требования: Авторизация пользователя.

2. **Аутентификация:**
   - URL: /login/
   - Описание: Позволяет пользователям войти в систему, используя свои учетные данные.

3. **Регистрация:**
   - URL: /register/
   - Описание: Позволяет пользователям зарегистрироваться в системе, создавая новый аккаунт.

4. **Выход из системы:**
   - URL: /logout/
   - Описание: Позволяет пользователям выйти из системы.

## Зависимости

Проект "black_order" использует следующие зависимости:

- Django 4.2.6
- Django-Bootstrap4 23.2
- Django-Widget-Tweaks 1.5.0
- Gunicorn 21.2.0
- Psycopg2 2.9.9
- Psycopg2-binary 2.9.9

## Развертывание для продакшена

Для развертывания приложения для продакшена выполните следующие шаги:

1. Сконфигурируйте Docker:
   ```bash
   docker-compose up --build
   ```

2. Запустите контейнер с проектом:
   ```bash
   sudo docker exec -it black_order bash -c "sh /app/entrypoint.sh"
   ```

Теперь проект "black_order" доступен для использования в продакшене.

**Примечание:** Перед развертыванием в продакшене убедитесь, что настройки базы данных и другие конфигурации соответствуют требованиям вашей среды.

## Завершение

Проект "black_order" предоставляет удобный способ управления информацией о продуктах и заказах. Он также включает в себя авторизацию и регистрацию пользователей для обеспечения безопасности данных.