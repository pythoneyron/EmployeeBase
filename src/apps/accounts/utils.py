# -*- coding: utf-8 -*-
from functools import reduce
from django.db.models import Q


def query_filter_users(alphabet_range):
    symbols = list('абвгдеёжзийклмнопрстуфхцчшщъыьэюя')
    alphabet_list = alphabet_range.lower().split('-')

    try:
        start_letter = symbols.index(alphabet_list[0])
        end_letter = symbols.index(alphabet_list[-1]) + 1
        if end_letter == 'я':
            symbols = symbols[start_letter:]
        else:
            symbols = symbols[start_letter:end_letter]
    except ValueError:
        pass
    query = reduce(lambda q, letter: q | Q(last_name__istartswith=letter), symbols, Q())
    return query
