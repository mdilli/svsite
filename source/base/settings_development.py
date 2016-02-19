
"""
These special settings are used in deveopment; they have extra requirements.
"""

from sys import argv, stderr
from settings import *


INSTALLED_APPS = tuple(INSTALLED_APPS) + (
	'sslserver',               # in debug mode only
	'django_extensions',       # for development (making docs)
)

if 'runserver' in argv:
	stderr.write('you should use ssl server:\n')
	stderr.write('python source/manage.py runsslserver localhost.markv.nl:8443\n')
	exit(1)


