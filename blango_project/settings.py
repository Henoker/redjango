from configurations import Configuration

from pathlib import Path

from configurations import values
import logging


class Dev(Configuration):
    # Build paths inside the project like this: BASE_DIR / 'subdir'.
    BASE_DIR = Path(__file__).resolve().parent.parent


    # Quick-start development settings - unsuitable for production
    # See https://docs.djangoproject.com/en/5.0/howto/deployment/checklist/

    # SECURITY WARNING: keep the secret key used in production secret!
    SECRET_KEY = "django-insecure--9rdt2r3ut&&2l+h_me1#o-1frkpguy_f&iy04a@d#=haxd%=g"

# SECURITY WARNING: don't run with debug turned on in production!
    DEBUG = True

    ALLOWED_HOSTS = []


    # Application definition

    INSTALLED_APPS = [
        "django.contrib.admin",
        "django.contrib.auth",
        "django.contrib.contenttypes",
        "django.contrib.sessions",
        "django.contrib.messages",
        "django.contrib.staticfiles",
    # local app
        "blog",
    # Third_party app
        "crispy_forms",
        "crispy_bootstrap5",
        "debug_toolbar",
    ]

    MIDDLEWARE = [
        "django.middleware.security.SecurityMiddleware",
        "django.contrib.sessions.middleware.SessionMiddleware",
        "django.middleware.common.CommonMiddleware",
        "django.middleware.csrf.CsrfViewMiddleware",
        "django.contrib.auth.middleware.AuthenticationMiddleware",
        "django.contrib.messages.middleware.MessageMiddleware",
        "django.middleware.clickjacking.XFrameOptionsMiddleware",
        "debug_toolbar.middleware.DebugToolbarMiddleware",
    ]
    
    INTERNAL_IPS = [
    # ...
    "127.0.0.1",
    # ...
    ]
    
    ROOT_URLCONF = "blango_project.urls"

    TEMPLATES = [
        {
            "BACKEND": "django.template.backends.django.DjangoTemplates",
            "DIRS": [BASE_DIR / 'templates'],
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

    WSGI_APPLICATION = "blango_project.wsgi.application"


    # Database
    # https://docs.djangoproject.com/en/5.0/ref/settings/#databases

    DATABASES = {
        "default": {
            "ENGINE": "django.db.backends.sqlite3",
            "NAME": BASE_DIR / "db.sqlite3",
        }
    }
    # Password Hashing 
    # Argon2 Password Hashing Algorithm
    PASSWORD_HASHERS = [
      'django.contrib.auth.hashers.Argon2PasswordHasher',
      'django.contrib.auth.hashers.PBKDF2PasswordHasher',
      'django.contrib.auth.hashers.PBKDF2SHA1PasswordHasher',
      'django.contrib.auth.hashers.BCryptSHA256PasswordHasher',
    ]

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

    TIME_ZONE = values.Value("UTC")
    
   

    USE_I18N = True

    USE_TZ = True


    # Static files (CSS, JavaScript, Images)
    # https://docs.djangoproject.com/en/5.0/howto/static-files/

    STATIC_URL = "static/"

    # Default primary key field type
    # https://docs.djangoproject.com/en/5.0/ref/settings/#default-auto-field

    DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"


    CRISPY_ALLOWED_TEMPLATE_PACKS = "bootstrap5"
    CRISPY_TEMPLATE_PACK = "bootstrap5"
    
    LOGGING = {
      "version": 1,
      "disable_existing_loggers": False,
      "filters": {
          "require_debug_false": {
              # Error Emails are only sent in production enviroments
              # The class below only passes messages through when DEBUG is False.
              "()": "django.utils.log.RequireDebugFalse",
          },
      },
      "formatters": {
          "verbose": {
              "format": "{levelname} {asctime} {module} {process:d} {thread:d} {message}",
              # Outputs the log level, time of the message (asctime), name of 
              # the module that generated the message, the process ID, 
              # thread ID, and lastly, the message.
              "style": "{",
            },
      },
      "handlers": {
          "console": {
              "class": "logging.StreamHandler", 
              "stream": "ext://sys.stdout",
              "formatter": "verbose",
          },
          "mail_admins": {
              "level": "ERROR", 
              "class": "django.utils.log.AdminEmailHandler",
              "filters": ["require_debug_false"],
          },
      },
      "loggers": {
          # Django.request so that only unhandled exceptions get sent.
          "django.request": {
              "handlers": ["mail_admins"],
              "level": "ERROR",
              # Add propagate: True; so the stack traces are logged to the console during development.
              "propagate": True,
          },
      },
      "root": {
          "handlers": ["console"],
          "level": "DEBUG",
      },
  }