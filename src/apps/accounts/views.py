from django.shortcuts import redirect
from django.views.generic import ListView, DetailView
from django.contrib.auth import logout as auth_logout
from django.views.generic.edit import View

from apps.accounts.models import User
from apps.accounts.choices import SectionUser


class ListUsersView(ListView):
    model = User
    template_name = 'accounts/users.html'
    paginate_by = 10
    context_object_name = 'users'

    def get_paginate_by(self, queryset):
        """ Динамически меняет вывод количества объектов на странице """
        return self.request.GET.get('paginate_by', self.paginate_by)

    def get_queryset(self):
        queryset = super(ListUsersView, self).get_queryset()
        section = self.request.GET.get('section')
        company = self.request.GET.get('company')

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
