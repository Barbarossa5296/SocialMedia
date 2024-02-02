from .email_password import email_host_pass
from pathlib import Path


# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/5.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-u&rl-vh4^mbio6(qh-k4lwe%3im4a@1&x(zq)4905i^cg(ddt2'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['127.0.0.1', 'localhost', 'happypirateship.ru']
INTERNAL_IPS = ['127.0.0.1']


# Application definition

INSTALLED_APPS = [

    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django_extensions',
    'temporary.apps.TemporaryConfig',
    'users.apps.UsersConfig',
    'bootstrap5',
    'social_django',

]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    # "django.middleware.cache.UpdateCacheMiddleware",
    'django.middleware.common.CommonMiddleware',
    # "django.middleware.cache.FetchFromCacheMiddleware",
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

# CACHE_MIDDLEWARE_ALIAS = 'default'
# CACHE_MIDDLEWARE_SECONDS = 10
# CACHE_MIDDLEWARE_KEY_PREFIX = 'happypirateship'

ROOT_URLCONF = 'SocialMediaProject.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR/'SocialMediaProject'/'templates',
                 ],
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

WSGI_APPLICATION = 'SocialMediaProject.wsgi.application'


# Database
# https://docs.djangoproject.com/en/5.0/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

CACHES = {
    "default": {
        "BACKEND": "django.core.cache.backends.dummy.DummyCache",
        # "BACKEND": "django.core.cache.backends.redis.RedisCache",
        # "LOCATION": "redis://127.0.0.1:6379",
    }
}

# Password validation
# https://docs.djangoproject.com/en/5.0/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/5.0/topics/i18n/

LANGUAGE_CODE = 'ru-RU'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True


STATIC_URL = 'static/'

MEDIA_ROOT = BASE_DIR / 'media'
MEDIA_URL = '/media/'


DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

LOGOUT_REDIRECT_URL = 'home'

AUTHENTICATION_BACKENDS = ['social_core.backends.github.GithubOAuth2',
                           'django.contrib.auth.backends.ModelBackend',
                           'users.authentication.EmailAuthBackend',]

EMAIL_BACKEND = "django.core.mail.backends.smtp.EmailBackend"
EMAIL_HOST = "smtp.yandex.ru"
EMAIL_PORT = 465
EMAIL_HOST_USER = "woolfee52@yandex.ru"
EMAIL_HOST_PASSWORD = email_host_pass  # generate your personally pass
EMAIL_USE_SSL = True

DEFAULT_FROM_EMAIL = EMAIL_HOST_USER
SERVER_EMAIL = EMAIL_HOST_USER
EMAIL_ADMIN = EMAIL_HOST_USER

AUTH_USER_MODEL = 'users.User'

DEFAULT_USER_IMAGE = MEDIA_URL + 'users/default.png'
