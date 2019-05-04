from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, BaseUserManager
from django.utils.translation import gettext as _
from django.core import validators

from apps.accounts.choices import SectionUser
from apps.company.models import Company


# create user in admin and create superuser in manage.py
class UserManager(BaseUserManager):
    def create_user(self, email, password=None):
        if not email:
            raise ValueError(_('Пользователь должен иметь адрес электронной почты'))

        user = self.model(
            email=UserManager.normalize_email(email),
            username=UserManager.normalize_email(email),
        )

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password):
        user = self.create_user(email, password=password)
        user.is_active = True
        user.is_admin = True
        user.is_staff = True
        user.is_superuser = True
        user.save(using=self._db)
        return user


class User(AbstractBaseUser, PermissionsMixin):
    username = models.CharField(verbose_name=_('Имя пользователя'), max_length=255, unique=True,
                                help_text=_('Обязательное поле. Не более 30 символов. '
                                            'Только буквы, цифры и символы @/./+/-/_.'),
                                validators=[
                                    validators.RegexValidator(r'^[\w.@+-]+$', (
                                        'Enter a valid username. This value may contain only letters, numbers '
                                        'and @/./+/-/_ characters.'
                                    ), 'invalid'), ],
                                error_messages={'unique': _("A user with that username already exists."), }
                                )
    first_name = models.CharField(verbose_name=_('Имя'), max_length=255)
    last_name = models.CharField(verbose_name=_('Фамилия'), max_length=255)
    middle_name = models.CharField(verbose_name=_('Отчество'), max_length=255)
    date_birth = models.DateField(verbose_name=_('Дата рождения'), blank=True, null=True)
    email = models.EmailField(verbose_name=_('E-mail'), max_length=255, unique=True)
    phone_number = models.CharField(verbose_name=_('Номер телефона'), max_length=12, unique=True)
    start_date = models.DateField(verbose_name=_('Дата начала работы'), blank=True, null=True)
    end_date = models.DateField(verbose_name=_('Дата окончания работы'), blank=True, null=True)
    position = models.CharField(verbose_name=_('Должность'), max_length=255)
    company = models.ForeignKey(Company, verbose_name=_('Компания'), related_name='users', blank=True, null=True,
                                on_delete=models.CASCADE)
    section = models.PositiveIntegerField(verbose_name=_('Отдел'), choices=SectionUser.CHOICES,
                                          default=SectionUser.Intern)
    is_staff = models.BooleanField(verbose_name=_('Персонал'), default=False)
    is_active = models.BooleanField(verbose_name=_('Активный'), default=False)

    objects = UserManager()

    USERNAME_FIELD = 'email'

    def get_full_name(self):
        full_name = '{first_name} {last_name} {middle_name}'.format(
            first_name=self.first_name, last_name=self.last_name, middle_name=self.middle_name
        )
        return full_name

    def get_short_name(self):
        short_name = '{last_name} {first_name}'.format(
            last_name=self.last_name, first_name=self.first_name,
        )
        return short_name

    class Meta:
        verbose_name = _('Пользователь')
        verbose_name_plural = _('Пользователи')
