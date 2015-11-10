"""
	General settings for the svSite project.

	Location specific settings can be set in settings_local.py .
"""

from os.path import dirname, abspath, join
from django.utils.translation import gettext_noop
from misc.functions.local_example import generate_local
from misc.settings import *


BASE_DIR = dirname(dirname(dirname(abspath(__file__))))

DATA_DIR = BASE_DIR

AUTH_USER_MODEL = 'member.Member'

ACCOUNT_USER_MODEL_USERNAME_FIELD = None
ACCOUNT_EMAIL_REQUIRED = True
ACCOUNT_USERNAME_REQUIRED = False
ACCOUNT_AUTHENTICATION_METHOD = 'email'

INSTALLED_APPS = (
	'base',  # on top because of base.html template
	'member',  # must be before cms
	'djangosecure',
	'raven.contrib.django.raven_compat',
	'djangocms_admin_style',
	'django.contrib.auth',
	'django.contrib.contenttypes',
	'django.contrib.sessions',
	'django.contrib.admin',
	'django.contrib.sites',  # for allauth (and possibly others)
	'django.contrib.sitemaps',  # for django-cms
	'django.contrib.staticfiles',
	'django.contrib.messages',
	'misc',
	'ctrl',
	'display_exceptions',
	'django_extensions',
	'debug_toolbar',
	'allauth',  # todo: this is version locked
	'allauth.account',
	'allauth.socialaccount',
	# 'allauth.socialaccount.providers.facebook',
	# 'allauth.socialaccount.providers.github',
	# 'allauth.socialaccount.providers.google',
	# 'allauth.socialaccount.providers.linkedin_oauth2',
	# 'allauth.socialaccount.providers.openid',
	# 'allauth.socialaccount.providers.stackexchange',
	'cms',
	'menus',
	'sekizai',
	'treebeard',
	#'djangocms_style',
	'djangocms_column',
	'djangocms_text_ckeditor',
	#'djangocms_file',
	'djangocms_googlemap',
	#'djangocms_inherit',
	'djangocms_link',
	#'djangocms_picture',
	#'djangocms_teaser',
	#'djangocms_video',
	'filer',
	'mptt',
	'easy_thumbnails',
	# 'cmsplugin_filer_file',   # todo: turn back on after fixed, currently breaks clean migrate
	# 'cmsplugin_filer_folder', # todo: idem
	# 'cmsplugin_filer_image',  # todo: idem
	# 'cmsplugin_filer_teaser', # todo: idem
	# 'cmsplugin_filer_video',  # todo: idem
	'reversion',
	'activity',
	'content',
	'teams',
	'hreflang',
	'django_cleanup',
	'birthdays',
	#'haystack',
	#'cms-search',  # todo: change-cms-search (with haystack)
)

MIDDLEWARE_CLASSES = (
	# debug toolbar added automatically
	'raven.contrib.django.raven_compat.middleware.Sentry404CatchMiddleware',  # log 404s
	'django.contrib.sessions.middleware.SessionMiddleware',
	'django.middleware.common.CommonMiddleware',
	'django.middleware.csrf.CsrfViewMiddleware',
	'django.middleware.clickjacking.XFrameOptionsMiddleware',
	'django.middleware.locale.LocaleMiddleware',
	#'django.middleware.doc.XViewMiddleware', #todo: turn back on? it moved
	'django.middleware.security.SecurityMiddleware',
	'django.contrib.auth.middleware.AuthenticationMiddleware',
	'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
	'django.contrib.messages.middleware.MessageMiddleware',
	'cms.middleware.user.CurrentUserMiddleware',
	'cms.middleware.page.CurrentPageMiddleware',
	'cms.middleware.toolbar.ToolbarMiddleware',
	'cms.middleware.language.LanguageCookieMiddleware',
	'misc.middleware.unique_urls.WwwSlashMiddleware',
	'display_exceptions.DisplayExceptionMiddleware',
)

ROOT_URLCONF = 'base.urls'

CMS_PLACEHOLDER_CONF = {}

TEMPLATES = [
	{
		'BACKEND': 'django.template.backends.django.DjangoTemplates',
		'DIRS': [],
		#'APP_DIRS': True,
		'OPTIONS': {
			'context_processors': (
				'django.template.context_processors.i18n',
				'django.template.context_processors.debug',
				'django.template.context_processors.request',
				'django.template.context_processors.media',
				'django.template.context_processors.csrf',
				'django.template.context_processors.tz',
				'django.template.context_processors.static',
				'django.contrib.auth.context_processors.auth',
				'sekizai.context_processors.sekizai',
				'cms.context_processors.cms_settings',
				'django.contrib.messages.context_processors.messages',
				'allauth.account.context_processors.account',
				'allauth.socialaccount.context_processors.socialaccount',
				'base.context.context_settings',
			),
			'loaders': (
				'django.template.loaders.app_directories.Loader',
				#'django.template.loaders.eggs.Loader'
			),
			'debug': True,
		},
	},
]

CMS_PERMISSION = True

CMS_MAX_PAGE_PUBLISH_REVERSIONS = 200

AUTHENTICATION_BACKENDS = (
	'django.contrib.auth.backends.ModelBackend',
	'allauth.account.auth_backends.AuthenticationBackend',
)

WSGI_APPLICATION = 'base.wsgi.application'

MIGRATION_MODULES = {
	'djangocms_column': 'djangocms_column.migrations_django',
	'djangocms_googlemap': 'djangocms_googlemap.migrations_django',
	'djangocms_inherit': 'djangocms_inherit.migrations_django',
	'djangocms_link': 'djangocms_link.migrations_django',
	'djangocms_style': 'djangocms_style.migrations_django',
	#'djangocms_file': 'djangocms_file.migrations_django',
	#'djangocms_picture': 'djangocms_picture.migrations_django',
	#'djangocms_teaser': 'djangocms_teaser.migrations_django',
	#'djangocms_video': 'djangocms_video.migrations_django',
	'cmsplugin_filer_file': 'cmsplugin_filer_file.migrations_django',
	'cmsplugin_filer_folder': 'cmsplugin_filer_folder.migrations_django',
	'cmsplugin_filer_image': 'cmsplugin_filer_image.migrations_django',
	'cmsplugin_filer_teaser': 'cmsplugin_filer_teaser.migrations_django',
	'cmsplugin_filer_video': 'cmsplugin_filer_video.migrations_django',
}

LANGUAGE_CODE = 'nl'

LANGUAGES = (
	('nl', ('Dutch')),  # using gettext_noop here causes a circular import
	('en', ('English')),
)

CMS_LANGUAGES = {
	1: [
		{
			'redirect_on_fallback': True,
			'code': 'nl',
			'hide_untranslated': False,
			'public': True,
			'name': ('Dutch'),  # using gettext_noop here causes a circular import
		},
		{
			'redirect_on_fallback': True,
			'code': 'en',
			'hide_untranslated': False,
			'public': True,
			'name': ('English'),
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

BASE_TEMPLATE = 'base.html'  # magic name, see template comment
BASE_EMAIL_TEMPLATE = 'base.html'

CMS_TEMPLATES = (
	('page.html', 'Page'),
	('feature.html', 'Page with Feature')
)

SEPARATOR = '&laquo;'

# this should all be done by apache, but as a fallback
SECURE_SSL_REDIRECT = True
SECURE_BROWSER_XSS_FILTER = True
SECURE_CONTENT_TYPE_NOSNIFF = True
SECURE_HSTS_SECONDS = 30  # todo set to large amount (seconds) to let people use only https for that duration (maybe not)
SECURE_HSTS_INCLUDE_SUBDOMAINS = True  # todo: correct?

SESSION_COOKIE_SECURE = True
CSRF_COOKIE_SECURE = True

SESSION_COOKIE_HTTPONLY = True
CSRF_COOKIE_HTTPONLY = True

SESSION_COOKIE_NAME = 'session'
CSRF_COOKIE_NAME = 'csrf'

LANGUAGE_COOKIE_NAME = 'lang'

CSRF_FAILURE_VIEW = 'base.errors.csrf_failure'

STATICFILES_DIRS = (join(BASE_DIR, 'dev', 'bower'),)

MESSAGE_STORAGE = 'django.contrib.messages.storage.session.SessionStorage'

FILER_ENABLE_LOGGING = True

FILER_IMAGE_USE_ICON = True

TEXT_SAVE_IMAGE_FUNCTION = 'cmsplugin_filer_image.integrations.ckeditor.create_image_plugin'

THUMBNAIL_HIGH_RESOLUTION = True

THUMBNAIL_PROCESSORS = (
	'easy_thumbnails.processors.colorspace',
	'easy_thumbnails.processors.autocrop',
	#'easy_thumbnails.processors.scale_and_crop',
	'filer.thumbnail_processors.scale_and_crop_with_subject_location',
	'easy_thumbnails.processors.filters',
)

LOGIN_URL = '/user/login/'
LOGIN_REDIRECT_URL = '/user/me/'

INTERNAL_IPS = ('127.0.0.1',)


try:
	from base.settings_local import *
except ImportError:
	generate_local(__file__, 'svsite', create=True, filename='settings_local.py')


