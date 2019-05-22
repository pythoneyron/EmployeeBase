import random
from django.shortcuts import redirect
from django.views.generic import ListView, DetailView
from django.contrib.auth import logout as auth_logout
from django.views.generic.edit import View
from django.db.utils import IntegrityError

from apps.accounts.models import User
from apps.accounts.choices import SectionUser
from apps.accounts.utils import query_filter_users
from apps.company.models import Company


class ListUsersView(ListView):
    model = User
    template_name = 'accounts/users.html'
    paginate_by = 5
    context_object_name = 'users'

    def get_paginate_by(self, queryset):
        """ Динамически меняет вывод количества объектов на странице """
        return self.request.GET.get('paginate_by', self.paginate_by)

    def get_queryset(self):
        queryset = super(ListUsersView, self).get_queryset()
        section = self.request.GET.get('section')
        company = self.request.GET.get('company')

        if 'alphabet' in self.request.path:
            alphabet_range = self.request.GET.get('alphabet_range')
            if alphabet_range:
                query = query_filter_users(alphabet_range)
                queryset = queryset.filter(query)
        else:
            if section:
                queryset = queryset.filter(section=section)
            if company:
                queryset = queryset.filter(company__title__icontains=company)
        return queryset

    def get_context_data(self, **kwargs):
        context = super(ListUsersView, self).get_context_data(**kwargs)
        context['paginate_by'] = self.request.GET.get('paginate_by', '')
        context['filter_company'] = self.request.GET.get('company', '')
        context['filter_section'] = self.request.GET.get('section')
        context['all_users'] = self.get_queryset().count()
        context['all_sections'] = SectionUser.CHOICES
        return context


class DetaiUsersView(DetailView):
    model = User
    template_name = 'accounts/user_detail.html'
    context_object_name = 'user'

    def get_context_data(self, **kwargs):
        context = super(DetaiUsersView, self).get_context_data(**kwargs)
        if 'pk' in self.kwargs:
            context['pk_user'] = self.kwargs['pk']
        return context


class LogoutFormView(View):
    """ Выход из профиля """

    def get(self, request):
        auth_logout(request)
        return redirect('/')


def init_data():
    file = open('names.txt', 'r')
    company = Company.objects.all()
    counter = 1
    positions = ['Менеджер по PR', 'Дизайнер', 'Администратор сайта', 'Дизайнер рекламы', 'Верстальщик',
                 'Web-интегратор', 'Python разработчик']
    for line in file:
        year_birth = random.randint(1980, 2000)
        year_start = random.randint(2000, 2019)
        phone = random.randint(79220000000, 79229999999)
        fio_list = line.split()
        try:
            User.objects.create(
                email=f'test{counter}@mail.ru',
                username=f'test{counter}@mail.ru',
                last_name=fio_list[0],
                first_name=fio_list[1],
                middle_name=fio_list[2],
                phone_number=f'+{phone}',
                date_birth=f'{year_birth}-01-01',
                start_date=f'{year_start}-05-05',
                is_active=True,
                position=random.choice(positions),
                company=random.choice(company),
                section=random.randint(0, len(SectionUser.CHOICES) - 1)
            )
        except IntegrityError:
            pass
        counter += 1


# init_data()
