"""
	General settings for the svSite project.

	Location specific settings can be set in settings_local.py .
"""

from os.path import dirname, abspath, join
from django.utils.translation import gettext_noop, gettext

BASE_DIR = dirname(dirname(dirname(abspath(__file__))))

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.8/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '=i6wddk2^%s^4&ic(4g0!_+1s_w5@vpm-u0b@6#7$_2%g^ngay'

DEBUG = True
TEMPLATE_DEBUG = DEBUG

ALLOWED_HOSTS = []

AUTH_USER_MODEL = 'member.svUser'

ACCOUNT_USER_MODEL_USERNAME_FIELD = None
ACCOUNT_EMAIL_REQUIRED = True
ACCOUNT_USERNAME_REQUIRED = False
ACCOUNT_AUTHENTICATION_METHOD = 'email'

CMS_PERMISSION = True

# Application definition

INSTALLED_APPS = (
	'svsite',
	'grappelli.dashboard',
	'grappelli',  # before admin
	'django.contrib.admin',
	'django.contrib.auth',
	'django.contrib.contenttypes',
	'django.contrib.sessions',
	'django.contrib.messages',
	'django.contrib.staticfiles',
	'django.contrib.sites',  # for allauth (and possibly others)
	'django.contrib.sitemaps',  # fpr django-cms
	'django_extensions',
	'debug_toolbar',
	'allauth',
	'allauth.account',
	'allauth.socialaccount',
	# 'allauth.socialaccount.providers.facebook',
	# 'allauth.socialaccount.providers.github',
	# 'allauth.socialaccount.providers.google',
	# 'allauth.socialaccount.providers.linkedin_oauth2',
	# 'allauth.socialaccount.providers.openid',
	# 'allauth.socialaccount.providers.stackexchange',
	# 'djangocms_admin_style',  # already have grappelli
	'djangocms_text_ckeditor',
	'cms',
	'menus',
	'sekizai',
	'treebeard',
	'djangocms_style',
	'djangocms_column',
	'djangocms_file',
	#'djangocms_flash',
	'djangocms_googlemap',
	'djangocms_inherit',
	'djangocms_link',
	'djangocms_picture',
	'djangocms_teaser',
	'djangocms_video',
	'reversion',
	'member',
	'activity',
	'content',
)

MIDDLEWARE_CLASSES = (
	# debug toolbar added automatically
	'django.contrib.sessions.middleware.SessionMiddleware',
	'django.middleware.common.CommonMiddleware',
	'django.middleware.csrf.CsrfViewMiddleware',
	'django.middleware.clickjacking.XFrameOptionsMiddleware',
	'django.middleware.locale.LocaleMiddleware',
	'django.middleware.doc.XViewMiddleware',
	# 'django.middleware.security.SecurityMiddleware',  #  todo turn back on in django 1.8
	'django.contrib.auth.middleware.AuthenticationMiddleware',
	'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
	'django.contrib.messages.middleware.MessageMiddleware',
	'cms.middleware.user.CurrentUserMiddleware',
	'cms.middleware.page.CurrentPageMiddleware',
	'cms.middleware.toolbar.ToolbarMiddleware',
	'cms.middleware.language.LanguageCookieMiddleware',
	'svsite.middleware.RemoveWwwMiddleware',
)

ROOT_URLCONF = 'svsite.urls'

CMS_PLACEHOLDER_CONF = {}

TEMPLATE_CONTEXT_PROCESSORS = [
	'django.core.context_processors.i18n',  # Todo: change 'core' to 'template' in 1.8
	'django.core.context_processors.debug',
	'django.core.context_processors.request',
	'django.core.context_processors.media',
	'django.core.context_processors.csrf',
	'django.core.context_processors.tz',
	'django.core.context_processors.static',
	'django.contrib.auth.context_processors.auth',
	'sekizai.context_processors.sekizai',
	'cms.context_processors.cms_settings'
	'django.contrib.messages.context_processors.messages',
	'allauth.account.context_processors.account',
	'allauth.socialaccount.context_processors.socialaccount',
	'svsite.context.context_settings',
]

TEMPLATES = [
	{
		'BACKEND': 'django.template.backends.django.DjangoTemplates',
		'DIRS': [],
		'APP_DIRS': True,
		'OPTIONS': {
			'context_processors': TEMPLATE_CONTEXT_PROCESSORS,
		},
	},
]

TEMPLATE_LOADERS = (
	'django.template.loaders.app_directories.Loader',
	'django.template.loaders.eggs.Loader'
)

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

MIGRATION_MODULES = {
	'djangocms_column': 'djangocms_column.migrations_django',
	'djangocms_flash': 'djangocms_flash.migrations_django',
	'djangocms_googlemap': 'djangocms_googlemap.migrations_django',
	'djangocms_inherit': 'djangocms_inherit.migrations_django',
	'djangocms_link': 'djangocms_link.migrations_django',
	'djangocms_style': 'djangocms_style.migrations_django',
	'djangocms_file': 'djangocms_file.migrations_django',
	'djangocms_picture': 'djangocms_picture.migrations_django',
	'djangocms_teaser': 'djangocms_teaser.migrations_django',
	'djangocms_video': 'djangocms_video.migrations_django'
}


# Internationalization
# https://docs.djangoproject.com/en/1.8/topics/i18n/

LANGUAGE_CODE = 'nl'

LANGUAGES = (
	('nl', gettext_noop('Dutch')),
	('en_GB', gettext_noop('English')),
)

CMS_LANGUAGES = {
	1: [
		{
			'redirect_on_fallback': True,
			'code': 'en_GB',
			'hide_untranslated': False,
			'public': True,
			'name': gettext_noop('en_GB'),
		},
		{
			'redirect_on_fallback': True,
			'code': 'nl',
			'hide_untranslated': False,
			'public': True,
			'name': gettext_noop('nl'),
		},
	],
	'default': {
		'redirect_on_fallback': True,
		'hide_untranslated': False,
		'public': True,
	},
}

TIME_ZONE = 'Europe/Amsterdam'

USE_I18N = True

USE_L10N = True

USE_TZ = True

SITE_ID = 1

BASE_TEMPLATE = 'base.html'  # magic name, see template comment
BASE_EMAIL_TEMPLATE = 'base.html'

CMS_TEMPLATES = (
	('page.html', 'Page'),
	('feature.html', 'Page with Feature')
)

SEPARATOR = '&laquo;'

# have strip-www middlware so don't turn this on
# PREPEND_WWW = True
APPEND_SLASH = True

#
SECURE_SSL_REDIRECT = True
SECURE_BROWSER_XSS_FILTER = True
SECURE_CONTENT_TYPE_NOSNIFF = True
SECURE_HSTS_SECONDS = 30  # set to large amount (seconds) to let people use https only for that duration (maybe not)
SECURE_HSTS_INCLUDE_SUBDOMAINS = True

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.8/howto/static-files/

STATIC_ROOT = join('..', 'static')
STATIC_URL = '/static/'

MEDIA_ROOT = join('..', 'media')
MEDIA_URL = '/media/'

GRAPPELLI_ADMIN_TITLE = 'Admin panel {0:s} svSite'.format(SEPARATOR)
GRAPPELLI_INDEX_DASHBOARD = 'svsite.dashboard.CustomIndexDashboard'

LOGIN_URL = '/account/login/'
LOGIN_REDIRECT_URL = '/member/me/'

INTERNAL_IPS = ('127.0.0.1',)

SESSION_COOKIE_SECURE = True
CSRF_COOKIE_SECURE = True

try:
	from .settings_local import *
except ImportError:
	pth = join(BASE_DIR, 'source', 'svsite', 'settings_local.py')
	try:
		with open(pth, 'w+') as fh:
			fh.write(
				'\n"""\n\tLocal settings for this specific instance of svSite (e.g. passwords, absolute paths, ...).\n"""\n')
		print('creating local settings file "{0:s}"'.format(pth))
	except OSError:
		print('could not create local settings file "{0:s}"'.format(path))
