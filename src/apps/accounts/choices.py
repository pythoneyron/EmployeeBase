# -*- coding:utf-8 -*-
from django.utils.translation import ugettext_lazy as _


class SectionUser:
    Programmer = 0
    Manager = 1
    Design = 2
    Intern = 3

    CHOICES = (
        (Programmer, _('Программист')),
        (Manager, _('Менеджер')),
        (Design, _('Дизайнер')),
        (Intern, _('Стажер'))
    )

