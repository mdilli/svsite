
Machine-specific settings
-------------------------------

Some settings are machine-dependent, so you need to create ``local.py`` containing these settings. This file should be in the same directory as ``settings.py``, so typically ``source/local.py``.

At least, your local settings should contain:

.. code-block:: python

	from os.path import dirname, join

	BASE_DIR = dirname(dirname(__file__))

	SITE_URL = 'svleo.markv.nl'  #todo: update url
	ALLOWED_HOSTS = [SITE_URL, 'localhost']

	SITE_DISP_NAME = 'svSite'  #todo: update site name and tagline
	SITE_DISP_TAGLINE = 'Make your own website for your group!'

	SECRET_KEY = ''  #todo: generate a long random string

	DATABASES = {  #todo: choose some database settings
		'default': {
			'ENGINE': 'django.db.backends.postgresql_psycopg2',
			'NAME': 'database',
			'USER': 'username',
			'PASSWORD': 'PASSWORD',
			'HOST': '127.0.0.1',
			'CONN_MAX_AGE': 120,
		}
	}
	# alternatively, as a deveopment database:
	# DATABASES = {
	# 	"default": {
	# 		"ENGINE": "django.db.backends.sqlite3",
	# 		"NAME": join(BASE_DIR, 'dev', 'data.sqlite3'),
	# 	}
	# }

	MEDIA_ROOT = join('data', 'media', 'svleo')
	STATIC_ROOT = join('data', 'static', 'svleo')
	CMS_PAGE_MEDIA_PATH = join(MEDIA_ROOT, 'cms')
	SV_THEMES_DIR = join(BASE_DIR, 'themes')

You can create a secret key using random.org_ (join both together), or generate a better one yourself with bash:

.. code-block:: bash

	</dev/urandom tr -dc '1234567890!@#$%&*--+=__qwertQWERTasdfgASDFGzxcvbZXCVB' | head -c 32

You might also want to have a look at some of these:

.. code-block:: python

	SV_DEFAULT_THEME = 'standard'

	TIME_ZONE = 'Europe/Amsterdam'
	LANGUAGE_CODE = 'nl'
	LANGUAGES = (
		('nl', ('Dutch')),  # using gettext_noop here causes a circular import
		('en', ('English')),
	)

	CACHES = {
		'default': {
			'BACKEND': 'django.core.cache.backends.memcached.MemcachedCache',
			'LOCATION': '127.0.0.1:11211',
		}
	}

	# You have to redifine TEMPLATES if you want to add a template path or change TEMPLATE_DEBUG

	INTERNAL_IPS = []  # these ips are treated differently if a problem occurs

	# more info: https://docs.djangoproject.com/en/dev/topics/logging/#configuring-logging
	LOGGING = {
		'version': 1,
		'disable_existing_loggers': False,
		'handlers': {
			'file': {
				'level': 'DEBUG',
				'class': 'logging.FileHandler',
				'filename': '/path/to/django/debug.log',  # change this path
			},
		},
		'loggers': {
			'django': {
				'handlers': ['file'],
				'level': 'DEBUG',
				'propagate': True,
			},
		},
	}

	SESSION_COOKIE_SECURE = CSRF_COOKIE_SECURE = False

	DEBUG = FILER_DEBUG = False

You can change other Django settings, particularly it might be worthwhile to have a look at globalization_ settings.


.. _random.org: https://www.random.org/passwords/?num=2&len=16&format=plain&rnd=new
.. _globalization: https://docs.djangoproject.com/en/dev/ref/settings/


