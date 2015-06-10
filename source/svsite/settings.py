
"""
	General settings for the svSite project.

	Location specific settings can be set in settings_local.py .
"""

from os.path import dirname, abspath, join


BASE_DIR = dirname(dirname(dirname(abspath(__file__))))

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.8/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '=i6wddk2^%s^4&ic(4g0!_+1s_w5@vpm-u0b@6#7$_2%g^ngay'

DEBUG = True

ALLOWED_HOSTS = []

AUTH_USER_MODEL = 'member.svUser'

ACCOUNT_USER_MODEL_USERNAME_FIELD = None
ACCOUNT_EMAIL_REQUIRED = True
ACCOUNT_USERNAME_REQUIRED = False
ACCOUNT_AUTHENTICATION_METHOD = 'email'


# Application definition

INSTALLED_APPS = (
	'svsite',
	'grappelli',  # before admin
	'django.contrib.admin',
	'django.contrib.auth',
	'django.contrib.contenttypes',
	'django.contrib.sessions',
	'django.contrib.messages',
	'django.contrib.staticfiles',
	'django.contrib.sites',  # for allauth (and possibly others)
	'django_extensions',
	'allauth',
	'allauth.account',
	'allauth.socialaccount',
	#'allauth.socialaccount.providers.facebook',
	#'allauth.socialaccount.providers.github',
	#'allauth.socialaccount.providers.google',
	#'allauth.socialaccount.providers.linkedin_oauth2',
	#'allauth.socialaccount.providers.openid',
	#'allauth.socialaccount.providers.stackexchange',
	'member',
)

MIDDLEWARE_CLASSES = (
	'django.contrib.sessions.middleware.SessionMiddleware',
	'django.middleware.common.CommonMiddleware',
	'django.middleware.csrf.CsrfViewMiddleware',
	'django.contrib.auth.middleware.AuthenticationMiddleware',
	'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
	'django.contrib.messages.middleware.MessageMiddleware',
	'django.middleware.clickjacking.XFrameOptionsMiddleware',
	'django.middleware.security.SecurityMiddleware',
	'svsite.middleware.RemoveWwwMiddleware',
)

ROOT_URLCONF = 'svsite.urls'

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
				'allauth.account.context_processors.account',
				'allauth.socialaccount.context_processors.socialaccount',
				'svsite.context.context_settings',
			],
		},
	},
]

AUTHENTICATION_BACKENDS = (
	'django.contrib.auth.backends.ModelBackend',
	'allauth.account.auth_backends.AuthenticationBackend',
)

WSGI_APPLICATION = 'svsite.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.8/ref/settings/#databases

DATABASES = {
	'default': {
		'ENGINE': 'django.db.backends.sqlite3',
		'NAME': join(BASE_DIR, 'data', 'default.sqlite3'),
	}
}


# Internationalization
# https://docs.djangoproject.com/en/1.8/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


SITE_ID = 1

BASE_TEMPLATE = 'base.html'  # magic name, see template comment
BASE_EMAIL_TEMPLATE = 'base.html'


# have strip-www middlware so don't turn this on
# PREPEND_WWW = True
APPEND_SLASH = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.8/howto/static-files/

STATIC_ROOT = '../static/'
STATIC_URL = '/static/'

GRAPPELLI_ADMIN_TITLE = 'Admin panel &#8212; <a href="/">go to homepage</a>'

LOGIN_URL = '/account/login/'
LOGIN_REDIRECT_URL = '/member/me/'

INTERNAL_IPS = ('127.0.0.1',)



try:
	from .settings_local import *
except ImportError:
	pth = join(BASE_DIR, 'source', 'svsite', 'settings_local.py')
	try:
		with open(pth, 'w+') as fh:
			fh.write('\n"""\n\tLocal settings for this specific instance of svSite (e.g. passwords, absolute paths, ...).\n"""\n')
		print('creating local settings file "{0:s}"'.format(pth))
	except OSError:
		print('could not create local settings file "{0:s}"'.format(path))



