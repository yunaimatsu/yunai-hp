from pathlib import Path
import os
from django.utils.translation import gettext_lazy as _

BASE_DIR = Path(__file__).resolve().parent.parent
SECRET_KEY = 'django-insecure-=(&-j)nze5jh=z@$a3fv*5+9ld3^pc+$zv-yp$uijw49=y9!8^'
DEBUG = False
ALLOWED_HOSTS = [".localhost", "127.0.0.1", '[::1]']
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'app_hp'
]
MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]
ROOT_URLCONF = 'prj_hp.urls'
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')],
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
WSGI_APPLICATION = 'prj_hp.wsgi.application'
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}
AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]

LANGUAGE_CODE = 'en'
TIME_ZONE = 'UTC'
USE_I18N = True
USE_TZ = True
LANGUAGES = [
    ('en', _('English')),
    ('fr', _('French')),
    ('es', _('Spanish')),
]
LOCALE_PATHS = [
    os.path.join(BASE_DIR, 'locale')
]

STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')
STATICFILES_DIRS = [
    os.path.join(BASE_DIR, 'static'),
]
STATIC_URL = '/static/'
# STATIC_ROOT下のSTATICFILES_DIRSで指定したディレクトリ、にあるファイルをcollectstaticコマンドで集めてSTATIC_URLで指定したディレクトリに配置する
# files collected by collectstatic
MEDIA_URL = '/media/'

MEDIA_ROOT = os.path.join(BASE_DIR, 'media') # files uploaded via a FileField or ImageField

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
