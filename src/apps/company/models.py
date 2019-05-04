from django.db import models
from django.utils.translation import gettext as _


class Company(models.Model):
    title = models.CharField(verbose_name=_('Название'), max_length=255)
    activity = models.CharField(verbose_name=_('Деятельность'), max_length=255)

    def __str__(self):
        return '{title}'.format(title=self.title)

    class Meta:
        verbose_name = _('Компания')
        verbose_name_plural = _('Компании')
