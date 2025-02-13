"""
Django settings for Devroup project.

Generated by 'django-admin startproject' using Django 2.2.4.

For more information on this file, see
https://docs.djangoproject.com/en/2.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/2.2/ref/settings/
"""

import os

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/2.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '@)u3_*r%iz90l9^*)xj9=ibrj(&x5062wkqlly9o!d(k-+umv!'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ["*"]

# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'allauth',
    'allauth.account',
    'allauth.socialaccount',
    'allauth.socialaccount.providers.google',
    'allauth.socialaccount.providers.kakao',
    'allauth.socialaccount.providers.github',
    'community',
    'user',
]

AUTHENTICATION_BACKENDS = (
    'django.contrib.auth.backends.ModelBackend',

    'allauth.account.auth_backends.AuthenticationBackend',
)

SOCIAL_AUTH_GOOGLE_OAUTH2_KEY = '903736009045-kqr5r3fpplu1b3i5n5fcn27s0d04mt1g.apps.googleusercontent.com'
SOCIAL_AUTH_GOOGLE_OAUTH2_SECRET = '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'

SOCIAL_AUTH_KAKAO_OAUTH2_KEY = 'b97834aa38f0fd9bd7a8f6946a4807c3'
SOCIAL_AUTH_KAKAO_OAUTH2_SECRET = 'qUvUrNCc5p4WDDikybYrbm9h1oDOD8X6'

SOCIAL_AUTH_GITHUB_OAUTH2_KEY = 'b319fd8a60f1cbbc4dd4'
SOCIAL_AUTH_GITHUB_OAUTH2_SECRET = '2ceb006b0f29ad06faf9eb486ae9d4ee6b6a2734'

SOCIALACCOUNT_PROVIDERS = {
    'google': {
        'SCOPE': [
            'profile',
            'email',
        ],
        'APP': {
            'client_id': SOCIAL_AUTH_GOOGLE_OAUTH2_KEY,
            'secret': SOCIAL_AUTH_GOOGLE_OAUTH2_SECRET,
            'key': '',
        }
    },

    'kakao': {
        'SCOPE': [
            'profile_nickname',
        ],
        'APP': {
            'client_id': SOCIAL_AUTH_KAKAO_OAUTH2_KEY,
            'secret': SOCIAL_AUTH_KAKAO_OAUTH2_SECRET,
            'key': '',
        }
    },

    'github': {
        'SCOPE': [
            'user',
        ],
        'APP': {
            'client_id': SOCIAL_AUTH_GITHUB_OAUTH2_KEY,
            'secret': SOCIAL_AUTH_GITHUB_OAUTH2_SECRET,
            'key': '',
        }
    }
}

MARKDOWNX_MARKDOWN_EXTENSIONS = [
    'markdown.extensions.extra',
    'markdown.extensions.codehilite',
    'markdown.extensions.tables',
    'markdown.extensions.admonition',
    'markdown.extensions.footnotes',
    'markdown.extensions.fenced_code',
    'markdown.extensions.nl2br',
    'markdown.extensions.sane_lists',
    'markdown.extensions.meta',
    'markdown.extensions.toc',
    'markdown.extensions.wikilinks',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'allauth.account.middleware.AccountMiddleware',
]

SOCIALACCOUNT_LOGIN_ON_GET = True

ACCOUNT_LOGOUT_ON_GET = True
LOGIN_REDIRECT_URL = 'community:post_list'
ROOT_URLCONF = 'Devroup.urls'

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
        },
    },
]

WSGI_APPLICATION = 'Devroup.wsgi.application'


# Database
# https://docs.djangoproject.com/en/2.2/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': os.environ.get('DB_NAME', 'devroup_db'),
        'USER': os.environ.get('DB_USER', 'devroup_user'),
        'PASSWORD': os.environ.get('DB_PASSWORD', 'devroup_password'),
        'HOST': os.environ.get('DB_HOST', 'db'),
        'PORT': os.environ.get('DB_PORT', '5432'),
    }
}

# Password validation
# https://docs.djangoproject.com/en/2.2/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/2.2/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'Asia/Seoul'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/2.2/howto/static-files/

STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'static')

MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
MEDIA_URL = '/media/'