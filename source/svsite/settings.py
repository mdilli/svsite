"""
	General settings for the svSite project.

	Location specific settings can be set in settings_local.py .
"""

from os.path import dirname, abspath, join
from django.utils.translation import gettext_noop, gettext


BASE_DIR = dirname(dirname(dirname(abspath(__file__))))
DATA_DIR = BASE_DIR

# Quick-start development settings - unsuitable for production

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'this-is-not-secret,-make-sure-to-put-your-key-in-settings_local.py'

DEBUG = True
TEMPLATE_DEBUG = DEBUG

ALLOWED_HOSTS = []

AUTH_USER_MODEL = 'member.svUser'

ACCOUNT_USER_MODEL_USERNAME_FIELD = None
ACCOUNT_EMAIL_REQUIRED = True
ACCOUNT_USERNAME_REQUIRED = False
ACCOUNT_AUTHENTICATION_METHOD = 'email'

CMS_PERMISSION = True

CMS_MAX_PAGE_PUBLISH_REVERSIONS = 200

# Application definition

INSTALLED_APPS = (
	'svsite',
	'member',
	#'grappelli.dashboard', #todo
	#'grappelli',  # before admin
	'djangocms_admin_style',  # already have grappelli
	'django.contrib.auth',
	'django.contrib.contenttypes',
	'django.contrib.sessions',
	'django.contrib.admin',
	'django.contrib.sites',  # for allauth (and possibly others)
	'django.contrib.sitemaps',  # fpr django-cms
	'django.contrib.staticfiles',
	'django.contrib.messages',
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
	'cms',
	'menus',
	'sekizai',
	'treebeard',
	'djangocms_style',
	'djangocms_column',
	'djangocms_text_ckeditor',
	#'djangocms_file',
	'djangocms_googlemap',
	'djangocms_inherit',
	#'djangocms_link',
	#'djangocms_picture',
	#'djangocms_teaser',
	#'djangocms_video',
	'filer',
	'mptt',
	'easy_thumbnails',
	'cmsplugin_filer_file',
	'cmsplugin_filer_folder',
	'cmsplugin_filer_link',
	'cmsplugin_filer_image',
	'cmsplugin_filer_teaser',
	'cmsplugin_filer_video',
	'reversion',
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
	'cms.context_processors.cms_settings',
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
	'djangocms_googlemap': 'djangocms_googlemap.migrations_django',
	'djangocms_inherit': 'djangocms_inherit.migrations_django',
	#'djangocms_link': 'djangocms_link.migrations_django',
	'djangocms_style': 'djangocms_style.migrations_django',
	#'djangocms_file': 'djangocms_file.migrations_django',
	#'djangocms_picture': 'djangocms_picture.migrations_django',
	#'djangocms_teaser': 'djangocms_teaser.migrations_django',
	#'djangocms_video': 'djangocms_video.migrations_django',
	'cmsplugin_filer_file': 'cmsplugin_filer_file.migrations_django',
	'cmsplugin_filer_folder': 'cmsplugin_filer_folder.migrations_django',
	'cmsplugin_filer_link': 'cmsplugin_filer_link.migrations_django',
	'cmsplugin_filer_image': 'cmsplugin_filer_image.migrations_django',
	'cmsplugin_filer_teaser': 'cmsplugin_filer_teaser.migrations_django',
	'cmsplugin_filer_video': 'cmsplugin_filer_video.migrations_django',
}


# Internationalization
# https://docs.djangoproject.com/en/1.8/topics/i18n/

LANGUAGE_CODE = 'nl'

LANGUAGES = (
	('nl', gettext_noop('Dutch')),
	('en', gettext_noop('English')),
)

CMS_LANGUAGES = {
	1: [
		{
			'redirect_on_fallback': True,
			'code': 'en',
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
STATIC_URL = '/s/'

MEDIA_ROOT = join('..', 'media')
#CMS_PAGE_MEDIA_PATH = join(MEDIA_ROOT, 'cms')
MEDIA_URL = '/d/'

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
	from random import choice
	from os import chmod
	pth = join(BASE_DIR, 'source', 'svsite', 'settings_local.py')
	try:
		with open(pth, 'w+') as fh:
			fh.write('"""\n\tLocal settings for this specific instance of svSite (e.g. passwords, absolute paths, ...).\n"""' + \
				'\n\nSECRET_KEY = "{0:s}"\n\n'.format(''.join([choice('abcdefghijklmnopqrstuvwxyz0123456789@#$%^&*(-_=+)') for i in range(50)])) +
				'DATABASES = {\n\t"default": {\n\t\t"ENGINE": "django.db.backends.sqlite3",\n\t\t"NAME": "' + join(BASE_DIR, 'data', 'default.sqlite3') + '",\n\t}\n}\n\n\n')
		chmod(pth, 0o640)
		print('creating local settings file "{0:s}"'.format(pth))
	except OSError:
		print('could not create local settings file "{0:s}"'.format(pth))


