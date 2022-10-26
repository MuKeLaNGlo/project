from tabnanny import verbose
from unittest.util import _MAX_LENGTH
from django.db import models

# Create your models here.

class User(models.Model):
    username = models.CharField(max_length=255, unique=True, verbose_name = 'логин')
    # phone_book = models.ForeignKey(PhoneBook, on_delete=models.CASCADE)
    birthday = models.DateField('Дата рождения')
    class Meta:
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'
    def __str__(self):
        return f'{self.username}, {self.birthday}'

class PhoneBook(models.Model):
    name = models.CharField('Имя',max_length=255)
    phone_number = models.CharField('Номер телефона', max_length=255)
    notes = models.TextField('Заметки', blank=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name = 'Пользователь')
    class Meta:
        verbose_name = 'Телефонная книга'
        verbose_name_plural = 'Телефонные книги'
    def __str__(self):
        return f'{self.name}, {self.phone_number}'