import os
from datetime import datetime
from pathlib import Path

import dj_database_url
from dotenv import load_dotenv

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = Path(__file__).resolve().parent.parent


load_dotenv(Path(BASE_DIR) / ".env")

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.2/howto/deployment/checklist/


ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    "blog.apps.BlogConfig",
    "django_cleanup.apps.CleanupConfig",
    "rest_framework",
    "markdownx",
    "storages",
]

MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "project.middleware.RedirectHostMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
]

ROOT_URLCONF = "project.urls"

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

WSGI_APPLICATION = "project.wsgi.application"

# Password validation
# https://docs.djangoproject.com/en/4.2/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/4.2/topics/i18n/

LANGUAGE_CODE = "ja"

TIME_ZONE = "Asia/Tokyo"

USE_I18N = True
USE_L10N = True
USE_TZ = True

# markdownx
MARKDOWNX_MARKDOWN_EXTENSIONS = [
    "markdown.extensions.extra",  # Table, Code highlight
    "markdown.extensions.toc",  # Table Of Contents
    "markdown.extensions.nl2br",  # Line break
]

# markdownx image save path
MARKDOWNX_MEDIA_PATH = datetime.now().strftime("markdownx/%Y/%m/%d")

# Without DRF BrouwsableAPI
REST_FRAMEWORK = {
    "DEFAULT_RENDERER_CLASSES": [
        "rest_framework.renderers.JSONRenderer",
    ]
}

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.2/howto/static-files/

PROJECT_ROOT = os.path.dirname(os.path.abspath(__file__))
STATIC_ROOT = os.path.join(PROJECT_ROOT, "static")
STATIC_URL = "/static/"

MEDIA_ROOT = os.path.join(BASE_DIR, "media")
MEDIA_URL = "/media/"

DEBUG = os.getenv("DEBUG", "0").lower() in ["true", "t", "1"]

SECRET_KEY = os.environ["SECRET_KEY"]

if DEBUG:
    DATABASES = {
        "default": {
            "ENGINE": "django.db.backends.postgresql",
            "NAME": "postgres",
            "USER": "user",
            "PASSWORD": "password",
            "HOST": "postgres",
            "PORT": "5432",
        }
    }
    # CORS
    INSTALLED_APPS += ["corsheaders"]
    MIDDLEWARE = ["corsheaders.middleware.CorsMiddleware"] + MIDDLEWARE
    CORS_ORIGIN_WHITELIST = (
        "http://127.0.0.1:8080",
        "http://localhost:8080",
    )

    # BrowsableAPI
    REST_FRAMEWORK["DEFAULT_RENDERER_CLASSES"].append("rest_framework.renderers.BrowsableAPIRenderer")


if not DEBUG:
    MIDDLEWARE += ["whitenoise.middleware.WhiteNoiseMiddleware"]

    ALLOWED_HOSTS = ["example.com"]
    DATABASE_URL = os.environ["DATABASE_URL"]
    DATABASES = {
        "default": dj_database_url.config(),
    }

    STATICFILES_STORAGE = "whitenoise.storage.CompressedManifestStaticFilesStorage"

    AWS_ACCESS_KEY_ID = os.environ["AWS_ACCESS_KEY_ID"]
    AWS_SECRET_ACCESS_KEY = os.environ["AWS_SECRET_ACCESS_KEY"]
    AWS_STORAGE_BUCKET_NAME = os.environ["AWS_STORAGE_BUCKET_NAME"]

    AWS_S3_CUSTOM_DOMAIN = "%s.s3-ap-northeast-1.amazonaws.com" % AWS_STORAGE_BUCKET_NAME

    AWS_LOCATION = "media"
    DEFAULT_FILE_STORAGE = "storages.backends.s3boto3.S3Boto3Storage"
    MEDIA_URL = "https://%s/%s/" % (AWS_S3_CUSTOM_DOMAIN, AWS_LOCATION)
    AWS_S3_FILE_OVERWRITE = False
    AWS_DEFAULT_ACL = None

    CSRF_TRUSTED_ORIGINS = ["example.com"]
