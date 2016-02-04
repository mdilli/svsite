
from os.path import dirname, join


BASE_DIR = dirname(dirname(__file__))

SITE_URL = 'localhost.markv.nl'
ALLOWED_HOSTS = [SITE_URL, 'localhost']

SECRET_KEY = '9zbQg,_*ZZ=+E+EdxDTAz82ER=ba0s58QF1**ZqQ9tDr1eZ#7@t9Q119!fgb&w41'

DATABASES = {
	'default': {
		'ENGINE': 'django.db.backends.sqlite3',
		'NAME': join(BASE_DIR, 'dev', 'data', 'data.sqlite3'),  #todo: TEMP
		# 'NAME': join(BASE_DIR, 'dev', 'data', 'project.db'),
	},
}

MEDIA_ROOT = join(BASE_DIR, 'dev', 'media')
STATIC_ROOT = join(BASE_DIR, 'dev', 'static')
CMS_PAGE_MEDIA_PATH = join(MEDIA_ROOT, 'cms')
SV_THEMES_DIR = join(BASE_DIR, 'themes')

SV_DEFAULT_THEME = 'standard'

CACHES = {
	'default': {
		'BACKEND': 'django.core.cache.backends.dummy.DummyCache',
	}
}

INTERNAL_IPS = ['127.0.0.1', '192.87.225.84',]

MINIMAL_LOG_AUTH_KEY = '4U95S-5PW3O88O68176MUF8621J4RVWL'
MINIMAL_LOG_URL = 'https://markv.nl/log/add'

# SESSION_COOKIE_SECURE = False
# CSRF_COOKIE_SECURE = False

DEBUG = True
FILER_DEBUG = DEBUG


