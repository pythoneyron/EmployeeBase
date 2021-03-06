# -*- coding:utf-8 -*-
from django import template

register = template.Library()


@register.simple_tag
def url_replace(request, field, value):
    dict_ = request.GET.copy()
    dict_[field] = str(value)
    return dict_.urlencode()
