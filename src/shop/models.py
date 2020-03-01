from django.db import models
from django.utils.translation import gettext as _


class Category(models.Model):
    class Meta:
        verbose_name = _('Категория')
        verbose_name_plural = _('Категории')


    title = models.CharField(
        verbose_name=_('Категория'),
        max_length=100
    )

    def __str__(self):
        return self.title


class Item(models.Model):
    class Meta:
        verbose_name = _('Товар')
        verbose_name_plural = _('Товары')

    category = models.ForeignKey(
        to='Category',
        verbose_name=_('Категория'),
        null=True,
        blank=True,
        on_delete=models.SET_NULL
    )

    title = models.CharField(
        verbose_name=_('Название'),
        max_length=100
    )

    price = models.DecimalField(
        verbose_name=_('Цена'),
        max_digits=8,
        decimal_places=2
    )

    def __str__(self):
        return f'{self.title} ({self.category.title})'
