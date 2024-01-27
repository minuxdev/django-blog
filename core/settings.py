import os
from pathlib import Path

from dotenv import load_dotenv

load_dotenv()

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/5.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = os.getenv("SECRET_KEY", "secret_key")

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ["localhost", "127.0.0.1", ".vercel.app"]
# Application definition

INSTALLED_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    "users",
    "blog",
    "tinymce",
]

MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "whitenoise.middleware.WhiteNoiseMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
]

ROOT_URLCONF = "core.urls"

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [BASE_DIR / "templates"],
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

WSGI_APPLICATION = "core.wsgi.application"


#
DATABASES = {
    "default": {
        "ENGINE": os.getenv("POSTGRES_ENGINE", "django.db.backends.sqlite3"),
        "NAME": os.getenv("POSTGRES_DATABASE", BASE_DIR / "db.sqlite3"),
        "PORT": 5432,
        "HOST": os.getenv("POSTGRES_HOST", "localhost"),
        "USER": os.getenv("POSTGRES_USER", ""),
        "PASSWORD": os.getenv("POSTGRES_PASSWORD", ""),
        "URL": os.getenv("POSTGRES_URL", "localhost"),
    }
}


# Password validation
# https://docs.djangoproject.com/en/5.0/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/5.0/topics/i18n/

LANGUAGE_CODE = "en-us"

TIME_ZONE = "UTC"

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/5.0/howto/static-files/

STATIC_URL = "static/"
STATICFILES_DIRS = [BASE_DIR / "static"]
STATIC_ROOT = os.path.join(BASE_DIR, "staticfiles_build", "static")
# STATIC_ROOT = BASE_DIR / "staticfiles_build" / "static"

MEDIA_URL = "media/"
# MEDIA_ROOT = os.path.join(BASE_DIR, "media")

# Default primary key field type
# https://docs.djangoproject.com/en/5.0/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"


TINYMCE_DEFAULT_CONFIG = {
    "theme": "silver",
    "resize": "false",
    "width": "100%",
    "height": "20rem",
    "menubar": "file edit view insert format tools table help",
    "toolbar": """
    undo redo | bold italic underline strikethrough | 
    fontselect fontsizeselect formatselect typography codesample | 
    alignleft aligncenter alignright alignjustify | blockquote numlist bullist checklist | 
    forecolor backcolor casechange permanentpen formatpainter removeformat | 
    pagebreak | charmap emoticons | fullscreen  preview save print | 
    insertfile image media pageembed template link anchor| 
    a11ycheck ltr rtl | showcomments addcomment code""",
    "plugins": """
    advlist autolink lists link image codesample charmap print preview anchor 
    searchreplace visualblocks code fullscreen insertdatetime media table 
    advcode help wordcount spellchecker typography""",
    "codesample_languages": [
        {"text": "Python", "value": "python"},
        {"text": "Bash", "value": "sh"},
        {"text": "Javascript", "value": "javascript"},
        {"text": "HTML/XML", "value": "markup"},
        {"text": "CSS", "value": "css"},
    ],
}

AUTH_USER_MODEL = "users.User"
EMAIL_BACKEND = "django.core.mail.backends.console.EmailBackend"
LOGIN_URL = "/users/login/"
LOGIN_REDIRECT_URL = "blog:home"


# ------------- SECURITY ----------------
CSRF_TRUSTED_ORIGINS = ["http://*", "https://*"]
CORS_ORIGIN_ALLOW_ALL = True
