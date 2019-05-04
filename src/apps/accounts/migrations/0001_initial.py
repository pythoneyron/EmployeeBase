# Generated by Django 2.2 on 2019-05-04 20:00

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('company', '0001_initial'),
        ('auth', '0011_update_proxy_permissions'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('username', models.CharField(error_messages={'unique': 'Пользователь с таким именем уже существует.'}, help_text='Обязательное поле. Не более 30 символов. Только буквы, цифры и символы @/./+/-/_.', max_length=255, unique=True, validators=[django.core.validators.RegexValidator('^[\\w.@+-]+$', 'Enter a valid username. This value may contain only letters, numbers and @/./+/-/_ characters.', 'invalid')], verbose_name='Имя пользователя')),
                ('first_name', models.CharField(max_length=255, verbose_name='Имя')),
                ('last_name', models.CharField(max_length=255, verbose_name='Фамилия')),
                ('middle_name', models.CharField(max_length=255, verbose_name='Отчество')),
                ('date_birth', models.DateField(verbose_name='Дата рождения')),
                ('email', models.EmailField(max_length=255, unique=True, verbose_name='E-mail')),
                ('phone_number', models.CharField(max_length=12, unique=True, verbose_name='Номер телефона')),
                ('start_date', models.DateField(blank=True, null=True, verbose_name='Дата начала работы')),
                ('end_date', models.DateField(blank=True, null=True, verbose_name='Дата окончания работы')),
                ('position', models.CharField(max_length=255, verbose_name='Должность')),
                ('section', models.PositiveIntegerField(choices=[(0, 'Программист'), (1, 'Менеджер'), (2, 'Дизайнер'), (3, 'Стажер')], default=3, verbose_name='Отдел')),
                ('is_staff', models.BooleanField(default=False, verbose_name='Персонал')),
                ('is_active', models.BooleanField(default=False, verbose_name='Активный')),
                ('company', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='users', to='company.Company', verbose_name='Компания')),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.Group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.Permission', verbose_name='user permissions')),
            ],
            options={
                'verbose_name': 'Пользователь',
                'verbose_name_plural': 'Пользователи',
            },
        ),
    ]
