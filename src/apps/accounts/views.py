from django.views.generic import ListView

from apps.accounts.models import User


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
        context['all_users'] = self.get_queryset().count()
        return context
