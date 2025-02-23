"""
File: settings.py
Created by: K. Zimmerman
Project: kc_royals_backend
Description:
- Configures Django settings for the project.
- Enables JWT authentication and role-based access control.
- Fixes `APPEND_SLASH` to ensure correct URL handling.
- Adds missing `TEMPLATES` configuration for Django Admin.
- Ensures static file handling for deployment.
- Fixes missing `ROOT_URLCONF` setting to resolve server issues.
"""

from pathlib import Path
from datetime import timedelta

# Define the base directory of the project
BASE_DIR = Path(__file__).resolve().parent.parent

# SECURITY SETTINGS
SECRET_KEY = "django-insecure-ix2uhx#o$8r&2#b2muv*gl!#&ut$da&8nb9)fgt@2t$m6(ogu8"
DEBUG = True
ALLOWED_HOSTS = ["127.0.0.1", "localhost"]

# INSTALLED APPLICATIONS
INSTALLED_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    "rest_framework",
    "rest_framework_simplejwt",
    "corsheaders",
    "players",
    "django_filters",  
]

# MIDDLEWARE CONFIGURATION
MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "corsheaders.middleware.CorsMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
]

# REST FRAMEWORK CONFIGURATION
REST_FRAMEWORK = {
    "DEFAULT_AUTHENTICATION_CLASSES": ("rest_framework_simplejwt.authentication.JWTAuthentication",),
    "DEFAULT_PERMISSION_CLASSES": ("rest_framework.permissions.IsAuthenticated",),
}

# JWT SETTINGS
SIMPLE_JWT = {
    "ACCESS_TOKEN_LIFETIME": timedelta(hours=1),
    "REFRESH_TOKEN_LIFETIME": timedelta(days=7),
    "ROTATE_REFRESH_TOKENS": True,
}

# CORS SETTINGS
CORS_ALLOWED_ORIGINS = ["http://localhost:3000"]

# DATABASE CONFIGURATION
DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": BASE_DIR / "db.sqlite3",
    }
}

# FIX: Ensure Django handles URLs correctly with or without trailing slashes
APPEND_SLASH = True  # This ensures requests without slashes redirect properly

# ROOT URL CONFIGURATION (Fixes missing setting error)
ROOT_URLCONF = "kc_royals_backend.urls"

# TEMPLATES CONFIGURATION (Required for Django Admin)
TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [],  # Add custom template directories here if needed
        "APP_DIRS": True,  # Ensures Django loads templates from installed apps
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

# STATIC FILES CONFIGURATION
STATIC_URL = "/static/"
STATICFILES_DIRS = [BASE_DIR / "static"]
STATIC_ROOT = BASE_DIR / "staticfiles"
