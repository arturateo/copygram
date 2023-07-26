from phonenumber_field.modelfields import PhoneNumberField
from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.translation import gettext_lazy as _

GENDER = [('man', 'Мужской'), ('woman', 'Женский')]


class User(AbstractUser):
    email = models.EmailField(_("email address"), blank=False, null=False, unique=True)
    avatar = models.ImageField(null=False, blank=False, upload_to='user_pick', verbose_name='Аватар')
    bio = models.TextField(max_length=300, blank=True, null=True, verbose_name='Информация о пользователе')
    phone = PhoneNumberField(null=True, blank=True, unique=True)
    gender = models.CharField(max_length=40, null=True, blank=True, verbose_name='Пол', choices=GENDER)

    class Meta:
        db_table = 'users'
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'

    def __str__(self):
        return f'{self.username}'

