
"""
These special settings are necessary because there's a migration conflict without them.

For a clean migration, follow these steps:
	python source/manage.py migrate --settings=base.settings_migration
	python source/manage.py migrate --settings=settings
"""

from settings import *

#todo: add instructions to documentation


INSTALLED_APPS = tuple(app for app in INSTALLED_APPS if (not 'cmsplugin_filer_' in app))



