from django.db import models
from django.contrib.auth.models import AbstractUser

class Guest(AbstractUser):
    phone_number = models.CharField('Телефон', max_length=15, blank=True)
    address = models.TextField('Адрес', blank=True)

    class Meta:
        verbose_name = 'Гость'
        verbose_name_plural = 'Гости'

    def __str__(self):
        return self.username

class Room(models.Model):
    ROOM_TYPES = [
        ('standard', 'Стандарт'),
        ('deluxe', 'Делюкс'),
        ('suite', 'Люкс'),
    ]
    number = models.CharField('Номер комнаты', max_length=10, unique=True)
    type = models.CharField('Тип номера', max_length=10, choices=ROOM_TYPES)
    price_per_night = models.DecimalField('Цена за ночь', max_digits=10, decimal_places=2)
    is_available = models.BooleanField('Доступен', default=True)
    description = models.TextField('Описание', blank=True)

    class Meta:
        verbose_name = 'Номер'
        verbose_name_plural = 'Номера'

    def __str__(self):
        return f"{self.number} ({self.get_type_display()})"

class Booking(models.Model):
    guest = models.ForeignKey(Guest, on_delete=models.CASCADE, related_name='bookings', verbose_name='Гость')
    room = models.ForeignKey(Room, on_delete=models.CASCADE, related_name='bookings', verbose_name='Номер')
    check_in_date = models.DateField('Дата заезда')
    check_out_date = models.DateField('Дата выезда')
    total_price = models.DecimalField('Общая стоимость', max_digits=10, decimal_places=2, blank=True)
    is_confirmed = models.BooleanField('Подтверждено', default=False)

    class Meta:
        verbose_name = 'Бронирование'
        verbose_name_plural = 'Бронирования'

    def save(self, *args, **kwargs):
        if self.check_in_date and self.check_out_date and self.room:
            days = (self.check_out_date - self.check_in_date).days
            if days > 0:
                self.total_price = days * self.room.price_per_night
        super().save(*args, **kwargs)

    def __str__(self):
        return f"Бронь {self.room} для {self.guest} ({self.check_in_date} - {self.check_out_date})"