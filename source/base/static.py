
"""
Update STATIC_ROOT and STATIC_URL based on whether Apache serves files.
The goal is to change the static url when the version is changed (to flush cash).
"""


from base64 import urlsafe_b64encode
from os.path import dirname, abspath, join
from struct import pack


gettext = lambda s: s  # djangocms translation voodoo

with open(join(dirname(abspath(__file__)), '..', '..', 'dev', 'VERSION')) as fh:
	parts = fh.read().strip().split('.')
	VERSION = int(parts[0]), int(parts[1]), int(parts[2]) if len(parts) > 2 else 0

VERSION_INT = 65536*VERSION[0] + 256*VERSION[1] + VERSION[2]
VERSION_HASH = urlsafe_b64encode(pack('=I', VERSION_INT)).rstrip(b'=').rstrip(b'A').decode('ascii')


def update_static_local(STATIC_ROOT, STATIC_URL):
	# STATIC_ROOT = join(STATIC_ROOT, VERSION_HASH)
	STATIC_URL = join(STATIC_URL, VERSION_HASH)
	if not STATIC_URL.endswith('/'):
		STATIC_URL += '/'
	return STATIC_ROOT, STATIC_URL


def update_static_apache(STATIC_ROOT, STATIC_URL):
	STATIC_ROOT = join(STATIC_ROOT, VERSION_HASH)
	STATIC_URL = join(STATIC_URL, VERSION_HASH)
	return STATIC_ROOT, STATIC_URL


