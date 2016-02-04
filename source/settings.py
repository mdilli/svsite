
from base64 import urlsafe_b64encode
from django.core.exceptions import ImproperlyConfigured
from django.core.urlresolvers import reverse_lazy
from os.path import dirname, abspath, join
from struct import pack


BASE_DIR = dirname(dirname(abspath(__file__)))
gettext = lambda s: s  # djangocms translation voodoo

with open(join(BASE_DIR, 'dev', 'VERSION')) as fh:
	parts = fh.read().strip().split('.')
	VERSION = int(parts[0]), int(parts[1]), int(parts[2]) if len(parts) > 2 else 0

DEBUG = False
TEMPLATE_DEBUG = DEBUG
FILER_DEBUG = DEBUG  # easy-thumbnail exceptions propagated?

INSTALLED_APPS = (
	'tweaks',               # should be before adminstyle and allauth
	'member',               # not sure if this needs to be on top but if there's a preference it's probably top.

	'django.contrib.auth',
	'django.contrib.contenttypes',
	'django.contrib.sessions',
	'django.contrib.messages', # required for cmd toolbar
	'django.contrib.staticfiles',
	'django.contrib.sites',    # required for some cms thing and allauth
	'django.contrib.sitemaps',

	'allauth',
	'allauth.account',
	'allauth.socialaccount',

	# providers: http://django-allauth.readthedocs.org/en/latest/providers.html (some need https)
	'allauth.socialaccount.providers.facebook',
	'allauth.socialaccount.providers.github',
	'allauth.socialaccount.providers.google',
	'allauth.socialaccount.providers.linkedin_oauth2',
	'allauth.socialaccount.providers.openid',
	# todo: cncz accounts

	'cms',                     # django CMS itself - must be after custom user model app #todo
	'sekizai',                 # for JavaScript and CSS management
	'treebeard',               # utilities for implementing a tree
	'menus',                   # helper for model independent hierarchical website navigation
	'djangocms_admin_style',   # for the admin skin. You **must** add 'djangocms_admin_style' in the list **before** 'django.contrib.admin'.
	'django.contrib.admin',    # must be after admin_style

	'djangocms_text_ckeditor', # order doesn't matter

	'filer',                   # for cms-filer
	'easy_thumbnails',         # for cms-filer
	'mptt',                    # for cms-filer

	'cmsplugin_filer_file',    # from cms-filer, special migration needed
	'cmsplugin_filer_folder',  # from cms-filer, special migration needed
	'cmsplugin_filer_link',    # from cms-filer, special migration needed
	'cmsplugin_filer_image',   # from cms-filer, special migration needed
	'cmsplugin_filer_teaser',  # from cms-filer, special migration needed
	'cmsplugin_filer_video',   # from cms-filer, special migration needed

	'djangocms_googlemap',
	'djangocms_inherit',
	'djangocms_link',
	'djangocms_snippet',
	'djangocms_style',
	'djangocms_column',
	'djangocms_grid',
	# 'djangocms_oembed',      # too outdated, doesn't work
	# 'djangocms_table',       # too outdated, doesn't work

	'birthdays',

	'django_cleanup',          # deletes files if their model is deleted or changed
	'reversion',

	'djangobower',
	'sslserver',               # in debug mode only

	'django_countries',

	'display_exceptions',

	'svfinance',

	'base',
	'theme',
	'badges',
	'slider',
)

MIDDLEWARE_CLASSES = (
	'django.middleware.cache.UpdateCacheMiddleware',
	'base.middleware.HardAddSlashStripWwwMiddleware',  # ideally before CommonMiddleware (faster)
	'cms.middleware.utils.ApphookReloadMiddleware',
	'django.contrib.sessions.middleware.SessionMiddleware',
	#'django.middleware.common.CommonMiddleware',  # useful? (it does append_slash so if I use that, keep it)
	'django.middleware.csrf.CsrfViewMiddleware',
	'django.contrib.auth.middleware.AuthenticationMiddleware',
	'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
	'django.contrib.messages.middleware.MessageMiddleware',
	'django.middleware.clickjacking.XFrameOptionsMiddleware',
	'django.middleware.security.SecurityMiddleware',  # useful?
	'django.middleware.locale.LocaleMiddleware',
	'cms.middleware.user.CurrentUserMiddleware',
	'cms.middleware.page.CurrentPageMiddleware',
	'cms.middleware.toolbar.ToolbarMiddleware',
	'cms.middleware.language.LanguageCookieMiddleware',
	'django.middleware.cache.FetchFromCacheMiddleware',
	'display_exceptions.DisplayExceptionMiddleware',    # low on list
)

BOWER_INSTALLED_APPS = (
	# 'bootstrap#3.3.6',
	'bootswatch-dist#3.3.6-simplex',
	'bootstrap3-typeahead#4.0.0',
	'jquery#2.2.0',
	'smartmenus#1.0.0',
	'MathJax#2.6.0',
	'd3#3.5.0',
	'c3#0.4.10',
)

ROOT_URLCONF = 'urls'
APPEND_SLASH = True  # CommonMiddleware is disabled, but CMS also checks this
CSRF_FAILURE_VIEW = 'base.views.csrf_failure'
FILER_CANONICAL_URL = 'canon/'  # url after filer/ for canonical urls
LOGIN_URL = reverse_lazy('account_login')
LOGIN_REDIRECT_URL = '/'  # todo: reverse cms home
LOGOUT_URL = reverse_lazy('account_logout')
ACCOUNT_LOGOUT_REDIRECT_URL = LOGIN_REDIRECT_URL

TEMPLATES = [
	{
		'BACKEND': 'django.template.backends.django.DjangoTemplates',
		'DIRS': [join(BASE_DIR, 'themes', 'templates')],
		# 'APP_DIRS': True,  # already implied by loaders
		'OPTIONS': {
			'context_processors': [
				'django.template.context_processors.debug',
				'django.template.context_processors.request',
				'django.contrib.auth.context_processors.auth',
				'django.contrib.messages.context_processors.messages',  #todo: needed?
				'theme.context.theme_context',
				'sekizai.context_processors.sekizai',
				'cms.context_processors.cms_settings',
				'minimal_logger.context.minimal_javascript_log',
			],
			'loaders': [
				'django.template.loaders.filesystem.Loader',
				'django.template.loaders.app_directories.Loader',
				'django.template.loaders.eggs.Loader',
			],
		},
	},
]

AUTH_USER_MODEL = 'member.Member'

AUTHENTICATION_BACKENDS = (
	'django.contrib.auth.backends.ModelBackend',
	'allauth.account.auth_backends.AuthenticationBackend',
)

ACCOUNT_USERNAME_REQUIRED = False
ACCOUNT_EMAIL_REQUIRED = False # todo: change?
ACCOUNT_AUTHENTICATION_METHOD = 'username_email'
ACCOUNT_CONFIRM_EMAIL_ON_GET = True
ACCOUNT_FORMS = {} # {‘login’: ‘myapp.forms.LoginForm’} # see also ACCOUNT_SIGNUP_FORM_CLASS and SOCIALACCOUNT_FORMS
#ACCOUNT_USER_MODEL_USERNAME_FIELD = 'username'  # this is login name
#ACCOUNT_USER_MODEL_EMAIL_FIELD = 'email'
ACCOUNT_PASSWORD_MIN_LENGTH = 7
ACCOUNT_LOGIN_ON_EMAIL_CONFIRMATION = True
ACCOUNT_SESSION_REMEMBER = True
SOCIALACCOUNT_QUERY_EMAIL = True

CMS_PERMISSION = True

CMS_TEMPLATES = (
	('get_theme.html', gettext('Standard template')),
)

# http://docs.django-cms.org/en/develop/reference/configuration.html#cms-placeholder-conf
# todo: CMS_PLACEHOLDER_CONF can configure which plugins are available where
# todo: placeholder conf needed to set language_fallback=True for plugins
CMS_PLACEHOLDER_CONF = {}

# DATABASES = {
# 	'default': {
# 		'ENGINE': 'django.db.backends.sqlite3',
# 		'NAME': join(BASE_DIR, 'dev', 'data.sqlite3'),
# 	},
# }

LOCALE_PATHS = (join(BASE_DIR, 'lang'),)

STATICFILES_FINDERS = (
	'django.contrib.staticfiles.finders.FileSystemFinder',
	'django.contrib.staticfiles.finders.AppDirectoriesFinder',
	'djangobower.finders.BowerFinder',
)
STATICFILES_DIRS = (join(BASE_DIR, 'themes', 'static'),)
BOWER_COMPONENTS_ROOT = join(BASE_DIR, 'dev', 'bower')  # 'bower_components' is added automatically

STATIC_ROOT = join(BASE_DIR, 'dev', 'static')  # overwritten later
MEDIA_ROOT  = join(BASE_DIR, 'dev', 'media')
CMS_MEDIA_ROOT = join(MEDIA_ROOT, 'cms')
CMS_PAGE_MEDIA_PATH = join(MEDIA_ROOT, 'page')

SV_THEMES_DIR = join(BASE_DIR, 'themes')
SV_DEFAULT_THEME = 'standard'

SLIDER_IMG_WIDTH = 1600
SLIDER_IMG_HEIGHT = 150

FILE_UPLOAD_PERMISSIONS = 0o640

SESSION_ENGINE = 'django.contrib.sessions.backends.cached_db'

EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'

MESSAGE_STORAGE = 'django.contrib.messages.storage.session.SessionStorage'

CACHES = {
	'default': {
		'BACKEND': 'django.core.cache.backends.memcached.MemcachedCache',
		'LOCATION': '127.0.0.1:11211',
	}
}

CMS_CACHE_DURATIONS = dict(
	content=60,
	menus=60*15,
	permissions=60*15,
)

WSGI_APPLICATION = 'wsgi.application'

LANGUAGE_CODE = 'nl'
LANGUAGES = (
	('nl', ('Dutch')),  # using gettext_noop here causes a circular import
	('en', ('English')),
	('zh', ('Chinese')),
)

default = dict(
	public=True,
	hide_untranslated=False,
	redirect_on_fallback=True,
)
CMS_LANGUAGES = {
	1: [
		dict(
			code='nl',
			name=gettext('Dutch'),
			fallbacks=['en', 'zh',],
			# fallback might or might not be related to an error so just keep it as a list
			**default
		),
		dict(
			code='en',
			name=gettext('English'),
			fallbacks=['nl', 'zh',],
			**default
		),
		dict(
			code='zh',
			name=gettext('Chinese'),
			fallbacks=['en', 'zh',],
			**default
		),
	],
	'default': default
}

TIME_ZONE = 'UTC'
USE_I18N = True
USE_L10N = True
USE_TZ = True
FIRST_DAY_OF_WEEK = 1

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.8/howto/static-files/

MEDIA_URL = '/media/'
CMS_MEDIA_PATH = 'cms/'
CMS_MEDIA_URL = '/media/cms/'
STATIC_URL = '/static/'

SITE_ID = 1

CMS_MAX_PAGE_PUBLISH_REVERSION = 200  # maximum reversions stored by reversion

THUMBNAIL_PROCESSORS = (  # easy_thumbnails for filer
	'easy_thumbnails.processors.colorspace',
	'easy_thumbnails.processors.autocrop',
	#'easy_thumbnails.processors.scale_and_crop',
	'filer.thumbnail_processors.scale_and_crop_with_subject_location',
	'easy_thumbnails.processors.filters',
)

THUMBNAIL_HIGH_RESOLUTION = True   # retina thumbnails from easy_thumbnail
TEXT_SAVE_IMAGE_FUNCTION='cmsplugin_filer_image.integrations.ckeditor.create_image_plugin'  # allow dragging images into the text editor
FILER_IMAGE_USE_ICON = True

ACCOUNT_DEFAULT_HTTP_PROTOCOL = 'https'

SESSION_COOKIE_NAME = 'session'
SESSION_COOKIE_HTTPONLY = True
SESSION_COOKIE_SECURE = True
SESSION_COOKIE_AGE = 60 * 60 * 24 * 15
SESSION_EXPIRE_AT_BROWSER_CLOSE = False
ACCOUNT_SESSION_COOKIE_AGE = SESSION_COOKIE_AGE

CSRF_COOKIE_NAME = 'validate'
CSRF_COOKIE_HTTPONLY = True
CSRF_COOKIE_SECURE = True
CSRF_COOKIE_AGE = 60 * 60 * 24 * 2

LANGUAGE_COOKIE_NAME = 'lang'
LANGUAGE_COOKIE_AGE = 60 * 60 * 24 * 60

LOGGING = {
	'version': 1,
	'disable_existing_loggers': False,
	'formatters': {
		'verbose': {'format': '%(levelname)s %(asctime)s %(module)s %(message)s'},
		'simple': {'format': '%(levelname)s %(message)s'},
	},
	'filters': {
		# 'require_debug_false': {
		# 	'()': 'django.utils.log.RequireDebugFalse',
		# },
		'require_debug_true': {
			'()': 'django.utils.log.RequireDebugTrue',
		},
	},
	'handlers': {
		'console': {
			'level': 'INFO',
			'filters': ['require_debug_true'],
			'class': 'logging.StreamHandler',
		},
		'minimallog': {
			'level': 'WARNING',
			'class': 'minimal_logger.MinimalLogHandler',
			'formatter': 'verbose',
			# 'logging_url': 'https://markv.nl/log/add',
			# 'auth_key': None,
			# 'filter': ['require_debug_false'],
		}
	},
	'loggers': {
		'django': {
			'handlers': ['console', 'minimallog',],
			'level': 'WARNING',
			'propagate': True,
		},
	}
}


try:
	from local import *
except ImportError:
	raise ImproperlyConfigured('local settings were not found, please create them; refer to the documentation for an example')


# It seems STATICFILES_STORAGE does not work with django-filer; it doesn't even let me use manage.py help anymore
# STATICFILES_STORAGE = 'django.contrib.staticfiles.storage.CachedStaticFilesStorage'  # ManifestStaticFilesStorage
# This adds a hash of the version to static path, to prevent incorrect caching.
# Not a great idea in the end because it doesn't work if static files refer to each other by absolute path.
VERSION_HASH = urlsafe_b64encode(pack('=I', 65536*VERSION[0] + 256*VERSION[1] + VERSION[2])).rstrip(b'=').rstrip(b'A')
STATIC_URL = '/static/{0:}/'.format(VERSION_HASH.decode('ascii'))
if DEBUG:
	STATIC_ROOT = join(BASE_DIR, 'dev', 'static')
else:
	STATIC_ROOT = join(BASE_DIR, 'dev', 'static', VERSION_HASH.decode('ascii'))


