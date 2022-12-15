from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils.translation import gettext_lazy as _

NULLABLE = {'null': True, 'blank': True}


class HHUser(AbstractUser):
    # Переопределил, чтобы поля нельзя было оставить пустыми
    first_name = models.CharField(_('first name'), max_length=150)
    last_name = models.CharField(_('last name'), max_length=150)
    password = models.CharField(_('password'), max_length=128)

    # Отчество
    patronymic = models.CharField(
        max_length=124,
        verbose_name='Отчество',
        **NULLABLE
    )
    is_company = models.BooleanField(
        default=False,
        verbose_name='Является компанией',
        help_text=_('Отметьте, если пользователь находится в роли работодателя')
    )
    is_candidate = models.BooleanField(
        default=False,
        verbose_name='Является соискателем',
        help_text=_('Отметьте, если пользователь находится в роли соискателя')
    )
    is_moderator = models.BooleanField(
        default=False,
        verbose_name='Является модератором',
        help_text=_('Отметьте, если пользователь находится в роли модератора')
    )

    # Не удаляем а делаем неактивным
    def delete(self, *args, **kwargs):
        self.is_active = False
        self.save()

    class Meta:
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'

    def __str__(self):
        return self.username
