
"""
These special settings are necessary because there's a migration conflict without them.

See the :doc:`documentation <install>` for info.
"""

from settings import *


INSTALLED_APPS = tuple(app for app in INSTALLED_APPS if (not 'cmsplugin_filer_' in app and not app == 'tweaks'))


