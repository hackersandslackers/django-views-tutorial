"""Django's settings."""
import mimetypes
from os import path, getenv
import environ

mimetypes.add_type("text/css", ".css", True)

env = environ.Env()
environ.Env.read_env()

# False if not in os.environ
DEBUG = env("DEBUG")

# Build paths inside the project like this: path.join(BASE_DIR, ...)
BASE_DIR = path.dirname(path.dirname(path.abspath(__file__)))
PROJECT_ROOT = path.dirname(path.abspath(__file__))

# Static files (CSS, JavaScript, Images)
STATIC_URL = "/static/"
STATIC_ROOT = path.join(BASE_DIR, "static")
STATICFILES_DIRS = [
    path.join(PROJECT_ROOT, "static"),
    path.join(BASE_DIR, "homepage/static"),
    path.join(BASE_DIR, "function_views/static"),
    path.join(BASE_DIR, "class_views/static"),
]

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = environ.get("SECRET_KEY")

# Basic config
ALLOWED_HOSTS = [
    "0.0.0.0",
    "127.0.0.1",
    "localhost",
    "127.0.0.1:8000",
    "django.hackersandslackers.app",
]

INTERNAL_IPS = [
    "127.0.0.1",
]
WSGI_APPLICATION = "django_views_tutorial.wsgi.application"

# Application definition
INSTALLED_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    "homepage",
    "function_views",
    "class_views",
    "model_views",
]

# Added middleware
MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
]

# URLs
ROOT_URLCONF = "django_views_tutorial.urls"

# Database
DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.mysql",
        "NAME": environ.get("DATABASE_NAME"),
        "USER": environ.get("DATABASE_USER"),
        "PASSWORD": environ.get("DATABASE_PASSWORD"),
        "HOST": environ.get("DATABASE_HOST"),
        "PORT": environ.get("DATABASE_PORT"),
    }
}

# Password validation
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

# Base template folder & templating engine
TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [path.join(BASE_DIR, "django_views_tutorial/templates/")],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
                "django.template.context_processors.static",
                "django.template.context_processors.media",
            ],
        },
    },
]

# Internationalization
LANGUAGE_CODE = "en-us"
TIME_ZONE = "EST"
USE_I18N = True
USE_L10N = True
USE_TZ = True

# Etc.
APPEND_SLASH = True

GITHUB_REPO = "https://github.com/hackersandslackers/django-views-tutorial"
