import os

DEBUG = False

ALLOWED_HOSTS = [
    'pythoneyron.pythonanywhere.com',
]

SITE_HOST = ''

# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.postgresql_psycopg2',
#         'NAME': os.getenv('POSTGRES_DB'),
#         'USER': os.getenv('POSTGRES_USER'),
#         'PASSWORD': os.getenv('POSTGRES_PASSWORD'),
#         'HOST': os.getenv('POSTGRES_HOST'),
#         'PORT': os.getenv('POSTGRES_PORT'),
#     }
# }

# settings for host PythonAnywhere
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'pythoneyron$employeebase_db',
        'USER': 'pythoneyron',
        'PASSWORD': 'Ajdnc67Jci702JCqcb',
        'HOST': 'pythoneyron.mysql.pythonanywhere-services.com',
    }
}