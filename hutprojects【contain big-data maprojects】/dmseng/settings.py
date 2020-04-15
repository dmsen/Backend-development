"""
Django settings for dmseng project.

Generated by 'django-admin startproject' using Django 1.11.

For more information on this file, see
https://docs.djangoproject.com/en/1.11/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.11/ref/settings/
"""

import os

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.11/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'immixzf^iep6^a0#42nqfvz^5@kzih0btub7geb^k%b(a=9ssh'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['*']
# Access-Control-Allow-Origin  = '*'
# Application definition



# import dwebsocket
# 为所有的URL提供websocket，如果只是单独的视图需要可以不选
# MIDDLEWARE_CLASSES=['dwebsocket.middleware.WebSocketMiddleware']

WEBSOCKET_ACCEPT_ALL=True  # 可以允许每一个单独的视图实用websockets

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'apps.app01',
    'corsheaders',
    'apps.gerenweb',
    'apps.lin',
    'ckeditor',
    'ckeditor_uploader',

]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'corsheaders.middleware.CorsMiddleware',
    'django.middleware.common.CommonMiddleware',
    # 'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]
CORS_ORIGIN_ALLOW_ALL = True
CORS_ALLOW_CREDENTIALS = True
ROOT_URLCONF = 'dmseng.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR,'templates')],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                'apps.app01.global_views.guid_info',
            ],
        },
    },
]

WSGI_APPLICATION = 'dmseng.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.11/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}


# Password validation
# https://docs.djangoproject.com/en/1.11/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/1.11/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.11/howto/static-files/

STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR,'col_static')
if not os.path.exists(STATIC_ROOT):
    os.mkdir(STATIC_ROOT)
# 静态文件查找路径，注意不要写错参数名
STATICFILES_DIRS = [os.path.join(BASE_DIR,'static')]
STATICFILES_DIRS = [os.path.join(BASE_DIR,'static')]
# 配置媒体文件路径
MEDIA_ROOT = os.path.join(BASE_DIR,'media')

if not os.path.exists(MEDIA_ROOT):
    os.mkdir(MEDIA_ROOT)

MEDIA_URL = '/media/'
THUMB_SIZE = 300


# CKEditor 配置
#真实了解为：media_url +ckedintor_upload_path
CKEDITOR_UPLOAD_PATH = 'ckeditor_upload'
CKEDITOR_CONFIGS = {
    'awesome_ckeditor': {
        'toolbar': 'Basic',
    },
    'default_ckeditor':{
        'toolbar': 'Full',
    },
    'default': {
        'toolbar': 'Full',
    },
}
