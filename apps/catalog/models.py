from django.contrib.auth import get_user_model
from django.db import models
from .mixins import IsActiveModel, UidPrimaryModel, TimeStampedModel

User = get_user_model()


class Category(IsActiveModel, UidPrimaryModel, TimeStampedModel):
    title = models.CharField(verbose_name="Название категории",
                             max_length=50,
                             null=False,
                             blank=False)
    manager = models.ForeignKey(to=User, on_delete=models.PROTECT, default=None)

    def __str__(self):
        return self.title


class Product(IsActiveModel, UidPrimaryModel, TimeStampedModel):
    title = models.CharField(verbose_name="Название товара",
                             max_length=50,
                             null=False,
                             blank=False)

    category = models.ForeignKey(to=Category,
                                 on_delete=models.DO_NOTHING)
    article = models.CharField('Артикул', max_length=250, db_index=True)
    description = models.TextField('Описание')
    price = models.DecimalField('Цена', max_digits=10, decimal_places=2)
    available = models.BooleanField('Наличие товара', default=True)

    def __str__(self):
        return self.title