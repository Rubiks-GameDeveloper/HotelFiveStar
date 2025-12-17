# HotelFiveStar

## Основные возможности

- Управление номерами (Room): просмотр, создание, редактирование, удаление (доступно персоналу)
- Управление бронированиями (Booking): создание, просмотр, редактирование, удаление
- Профили гостей (Guest): просмотр и редактирование своего профиля
- Обязательная аутентификация через **JWT-токены** (SimpleJWT)
- Пагинация во всех списочных эндпоинтах
- Полная интерактивная документация через **Swagger UI** с поддержкой авторизации
- Разделение прав доступа:
  - **Guests** — обычные гости (видят только свои данные и номера)
  - **HotelStaff** — персонал отеля (полный доступ ко всем данным)

## Технологии

- Python 3.10+
- Django 4.x
- Django REST Framework
- djangorestframework-simplejwt (JWT-аутентификация)
- drf-yasg (Swagger-документация)
- SQLite

## Структура проекта

```
HotelFiveStar/
├── hotel_app/
│   ├── migrations/          # Миграции БД
│   ├── __init__.py
│   ├── admin.py             # Регистрация моделей в админке
│   ├── apps.py
│   ├── models.py            # Модели: Guest, Room, Booking
│   ├── serializers.py       # Сериализаторы для API
│   ├── views.py             # ViewSet'ы с логикой доступа
│   └── tests.py
├── hotel_project/
│   ├── __init__.py
│   ├── settings.py          # Настройки проекта (JWT, DRF, Swagger)
│   ├── urls.py              # Маршруты API и Swagger
│   ├── wsgi.py
│   └── asgi.py
├── manage.py
├── db.sqlite3               # База данных (SQLite)
├── README.md                # Этот файл
└── .gitignore
```

## Установка и запуск

1. Склонируйте репозиторий
   ```bash
   git clone https://github.com/Rubiks-GameDeveloper/HotelFiveStar.git
   cd HotelFiveStar
   ```

2. Создайте и активируйте виртуальное окружение
   ```bash
   python -m venv venv
   # или
   venv\Scripts\activate       # Windows
   ```

3. Установите зависимости
   ```bash
   pip install -r requirements.txt
   ```

4. Примените миграции
   ```bash
   python manage.py migrate
   ```

5. Создайте суперпользователя (для админки и тестирования персонала)
   ```bash
   python manage.py createsuperuser
   ```

6. Запустите сервер разработки
   ```bash
   python manage.py runserver
   ```

## Доступ к API

- **Swagger-документация**: http://127.0.0.1:8000/swagger/  
  (интерактивное тестирование всех эндпоинтов с кнопкой Authorize)

- **Админ-панель Django**: http://127.0.0.1:8000/admin/

### Основные эндпоинты

- `POST /api/token/` — получение JWT-токена (логин/пароль)
- `POST /api/token/refresh/` — обновление access-токена
- `GET /api/rooms/` — список номеров (пагинация)
- `GET /api/guests/` — профиль текущего пользователя
- `GET /api/bookings/` — список бронирований (свои или все — зависит от роли)

## Авторизация

Все эндпоинты требуют JWT-токена в заголовке:

```
Authorization: Bearer <ваш_access_токен>
```

1. Получите токен через `/api/token/` (POST с username и password)
2. В Swagger нажмите **Authorize** → введите `Bearer <токен>` (с пробелом!)

## Тестирование

- Создайте обычного пользователя через `python manage.py shell` или админку
- Назначьте пользователей в группы **Guests** или **HotelStaff** в админке для разделения прав

---