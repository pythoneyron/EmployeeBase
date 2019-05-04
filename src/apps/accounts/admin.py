from django.contrib import admin

from apps.accounts.models import User


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    fieldsets = (
        (None, {'fields': ('email', 'password')}),
        ('Personal info', {'fields': ('first_name', 'last_name', 'middle_name', 'phone_number', 'position',
                                      'section', 'company')}),
        ('Permissions', {'fields': ('is_active', 'is_staff', 'is_superuser',)}),
        ('Important dates', {'fields': ('last_login', 'date_birth', 'start_date', 'end_date')}),
    )

    list_display = ('email', 'last_name', 'first_name', 'section', 'is_active')
    search_fields = ('id', 'email', 'first_name', 'last_name', )
    list_filter = ('is_active', 'section')
    list_editable = ('is_active', 'section')
