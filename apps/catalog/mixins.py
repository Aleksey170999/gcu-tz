import uuid

from django.db import models
from django.db.models import Max, QuerySet
from django.utils.timezone import now
from django.utils.translation import gettext as _


class TimeStampedModel(models.Model):
    """
    Модель с датой и временем создания и изменения
    """
    created = models.DateTimeField(default=now, null=True, verbose_name=_('Когда создан'), editable=False)
    modified = models.DateTimeField(auto_now=True, null=True, verbose_name=_('Когда изменён'))

    @classmethod
    def get_last_modified(cls, qs: QuerySet = None) -> dict:
        if not qs:
            qs = cls.objects.all()
        return qs.aggregate(max_modified=Max('modified'))['max_modified']

    class Meta:
        abstract = True


class UidPrimaryModel(models.Model):
    """
    Объект с UUID первичным ключём
    """
    uid = models.UUIDField(_('UID'), default=uuid.uuid4, editable=False, primary_key=True)

    class Meta:
        abstract = True


class IsActiveModel(models.Model):
    """
    Активность
    """
    is_active = models.BooleanField(_('Активно'), default=True)

    class Meta:
        abstract = True
