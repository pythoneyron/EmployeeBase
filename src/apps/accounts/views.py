from django.shortcuts import render
from django.views.generic import ListView

from apps.accounts.models import User


class ListUsersView(ListView):
    model = User
    template_name = 'accounts/users.html'
    paginate_by = 10
    context_object_name = 'users'
