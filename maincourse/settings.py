"""
Django settings for maincourse project.

Generated by 'django-admin startproject' using Django 4.2.

For more information on this file, see
https://docs.djangoproject.com/en/4.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/4.2/ref/settings/
"""

from pathlib import Path
import os

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = ''

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True


ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'mainapp',
    'django_extensions',
    'django_summernote',
    'admin_reorder',

]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'django.middleware.locale.LocaleMiddleware',
    'admin_reorder.middleware.ModelAdminReorder',
]

ROOT_URLCONF = 'maincourse.urls'

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
            'libraries': {
                'custom_filters': 'mainapp.custom_filters',  # Путь к вашему файлу с фильтрами
            },
        },
    },
]

WSGI_APPLICATION = 'maincourse.wsgi.application'


# Database
# https://docs.djangoproject.com/en/4.2/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'store_db',
        'USER': 'postgres',
        'PASSWORD': '123123',
        'HOST': 'localhost',
        'PORT': '5432'
    }
}

# Password validation
# https://docs.djangoproject.com/en/4.2/ref/settings/#auth-password-validators

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


# Internationalization
# https://docs.djangoproject.com/en/4.2/topics/i18n/

LANGUAGE_CODE = 'ru-ru'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.2/howto/static-files/




# Default primary key field type
# https://docs.djangoproject.com/en/4.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

STATIC_URL = '/static/'

MEDIA_URL = '/media/'

  

if DEBUG:
  STATICFILES_DIRS = [os.path.join(BASE_DIR, 'static')]

else:
  STATIC_ROOT = os.path.join(BASE_DIR, 'static')

  

MEDIA_ROOT = os.path.join(BASE_DIR, 'media')

   

X_FRAME_OPTIONS = 'SAMEORIGIN'


ADMIN_REORDER = (
  'auth',
  {
    'app': 'mainapp',
    'models': ('mainapp.document', 'mainapp.Obuch', 'mainapp.Obuch_Desc', 'mainapp.Activities', 'mainapp.program_teacher', 'mainapp.Program', 'mainapp.Format', 'mainapp.Program_sod',),
    'label': 'Обучение',
  },
  {
    'app': 'mainapp',
    'models': ('mainapp.articles_inner', 'mainapp.Otrasl', 'mainapp.GroupSpec', 'mainapp.FilterArticle', 'mainapp.StatusArticle', 'mainapp.TegiNews', 'mainapp.tip_news',),
    'label': 'Статья'
  },
  {
    'app': 'mainapp',
    'models': ('mainapp.service', 'mainapp.Collections_watches',),
    'label': 'Сервис'
  },
  {
    'app': 'mainapp',
    'models': ('mainapp.Cases', 'mainapp.Teg',),
    'label': 'Кейсы'
  },
  {
    'app': 'mainapp',
    'models': ('mainapp.Person', 'mainapp.Personteg',),
    'label': 'Команда'
  },
  {
    'app': 'mainapp',
    'models': ('mainapp.About',),
    'label': 'О нас'
  },
  {
    'app': 'mainapp',
    'models': ('mainapp.Partners', 'mainapp.Form_Home',),
    'label': 'Главная'
  },
  {
    'app': 'mainapp',
    'models': ('mainapp.News', 'mainapp.TegiNews', 'mainapp.tip_news',),
    'label': 'Новости'
  }
)
