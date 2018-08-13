import os
from utils import env_as_bool, env_as_list, env_as_str

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

SECRET_KEY = env_as_str('SECRET_KEY', 'changeme')
DEBUG = env_as_bool('DEBUG')
ALLOWED_HOSTS = env_as_list('ALLOWED_HOSTS', '*' if DEBUG else '')

MY_APPS = [
    'dots',
]

THIRD_APPS = [
    'django_brfied',
    'rest_framework',
    'django_extensions'
]

DJANGO_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
]

INSTALLED_APPS = MY_APPS + THIRD_APPS + DJANGO_APPS

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'wsgi.application'

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite'),
    }
}

AUTH_USER_MODEL = 'dots.Colaborador'


# Example:
# 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator,'
# 'django.contrib.auth.password_validation.MinimumLengthValidator,'
# 'django.contrib.auth.password_validation.CommonPasswordValidator,'
# 'django.contrib.auth.password_validation.NumericPasswordValidator'
AUTH_PASSWORD_VALIDATORS = [{'NAME': v} for v in env_as_list('AUTH_PASSWORD_VALIDATORS', '') if v != '']

LANGUAGE_CODE = env_as_str('LANGUAGE_CODE', 'pt-br')
TIME_ZONE = env_as_str('TIME_ZONE', 'UTC')
USE_I18N = env_as_bool('USE_I18N')
USE_L10N = env_as_bool('USE_L10N')
USE_TZ = env_as_bool('USE_TZ')

STATIC_URL = env_as_str('STATIC_URL', '/static/')


REST_FRAMEWORK = {
    'DEFAULT_PERMISSION_CLASSES': [
        'rest_framework.permissions.DjangoModelPermissionsOrAnonReadOnly'
    ]
}
