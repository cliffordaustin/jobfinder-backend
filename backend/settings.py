"""
Django settings for backend project.

Generated by 'django-admin startproject' using Django 3.2.6.

For more information on this file, see
https://docs.djangoproject.com/en/3.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/3.2/ref/settings/
"""

from pathlib import Path
import os
from environs import Env

import subprocess
import ast


def get_environ_vars():
    try:
        # Run the get-config command to fetch environment variables
        completed_process = subprocess.run(
            ["/opt/elasticbeanstalk/bin/get-config", "environment"],
            stdout=subprocess.PIPE,
            text=True,
            check=True,
        )
        print("completed process", ast.literal_eval(completed_process.stdout))
        print(
            "completed process type", type(ast.literal_eval(completed_process.stdout))
        )
        print(
            "Secret key 1", ast.literal_eval(completed_process.stdout).get("SECRET_KEY")
        )
        print("Secret key 2", ast.literal_eval(completed_process.stdout)["SECRET_KEY"])
        return ast.literal_eval(completed_process.stdout)
    except Exception as e:
        print(f"Error fetching environment variables: {e}")
        return {}


env = Env()
env.read_env(path=".env", override=True)

env_vars = get_environ_vars()


# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = env_vars.get("SECRET_KEY", env("SECRET_KEY"))

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = env.bool("DEBUG", default=False)

ALLOWED_HOSTS = [
    "localhost",
    "jobfinder-env.eba-twqe3t6p.us-west-2.elasticbeanstalk.com",
]

INSTALLED_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    "django.contrib.sites",
    "allauth",
    "allauth.account",
    "allauth.socialaccount",
    "allauth.socialaccount.providers.google",
    "allauth.socialaccount.providers.facebook",
    "rest_framework",
    "rest_framework.authtoken",
    "dj_rest_auth",
    "dj_rest_auth.registration",
    "phonenumber_field",
    "django_filters",
    "imagekit",
    "users",
    "jobs",
    "company",
    "storages",
    "django_cleanup.apps.CleanupConfig",  # should be placed last
]


REST_FRAMEWORK = {
    "DEFAULT_FILTER_BACKENDS": ["django_filters.rest_framework.DjangoFilterBackend"],
    "DEFAULT_PAGINATION_CLASS": "rest_framework.pagination.LimitOffsetPagination",
    "PAGE_SIZE": 100,
    "DEFAULT_AUTHENTICATION_CLASSES": [
        "rest_framework.authentication.TokenAuthentication",
    ],
}


MIDDLEWARE = [
    "corsheaders.middleware.CorsMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.security.SecurityMiddleware",
    "whitenoise.middleware.WhiteNoiseMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
    "allauth.account.middleware.AccountMiddleware",
]

CORS_ALLOW_ALL_ORIGINS = True

ROOT_URLCONF = "backend.urls"

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
            ],
        },
    },
]

WSGI_APPLICATION = "backend.wsgi.application"


AUTHENTICATION_BACKENDS = [
    "django.contrib.auth.backends.ModelBackend",
    "allauth.account.auth_backends.AuthenticationBackend",
]


AUTH_USER_MODEL = "users.CustomUser"


REST_AUTH = {
    "REGISTER_SERIALIZER": "users.api.serializer.RegisterSerializer",
}

# Database
# https://docs.djangoproject.com/en/3.2/ref/settings/#databases

DATABASES = {"default": env_vars.get("DATABASE_URL", env.dj_db_url("DATABASE_URL"))}

# Password validation
# https://docs.djangoproject.com/en/3.2/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        "NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.MinimumLengthValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.CommonPasswordValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.NumericPasswordValidator",
    },
]


# Internationalization
# https://docs.djangoproject.com/en/3.2/topics/i18n/

LANGUAGE_CODE = "en-us"

TIME_ZONE = "UTC"

USE_I18N = True

USE_L10N = True

USE_TZ = True


# https://docs.djangoproject.com/en/3.2/ref/settings/#default-auto-field

STATIC_URL = "/static/"  # Path for serving static files
STATIC_ROOT = os.path.join(BASE_DIR, "static")  #

MEDIA_ROOT = os.path.join(BASE_DIR, "media")
MEDIA_URL = "/media/"

DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"

SITE_ID = 1

EMAIL_BACKEND = "django.core.mail.backends.console.EmailBackend"
ACCOUNT_EMAIL_VERIFICATION = "optional"

ACCOUNT_AUTHENTICATION_METHOD = "email"
ACCOUNT_EMAIL_REQUIRED = True
ACCOUNT_UNIQUE_EMAIL = True
ACCOUNT_USERNAME_REQUIRED = False
ACCOUNT_USER_MODEL_USERNAME_FIELD = None

AWS_ACCESS_KEY_ID = env_vars.get("AWS_ACCESS_KEY_ID", env("AWS_ACCESS_KEY_ID"))
AWS_SECRET_ACCESS_KEY = env_vars.get(
    "AWS_SECRET_ACCESS_KEY", env("AWS_SECRET_ACCESS_KEY")
)
AWS_STORAGE_BUCKET_NAME = env_vars.get(
    "AWS_STORAGE_BUCKET_NAME", env("AWS_STORAGE_BUCKET_NAME")
)
AWS_S3_REGION_NAME = env_vars.get("AWS_S3_REGION_NAME", env("AWS_S3_REGION_NAME"))
AWS_S3_CUSTOM_DOMAIN = f"{AWS_STORAGE_BUCKET_NAME}.s3.amazonaws.com"

AWS_S3_FILE_OVERWRITE = False

STORAGES = {
    "default": {
        "BACKEND": "storages.backends.s3boto3.S3Boto3Storage",
    },
    "staticfiles": {
        "BACKEND": "storages.backends.s3boto3.S3StaticStorage",
    },
}
