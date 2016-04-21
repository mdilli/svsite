
from genericpath import isfile
from os import access, W_OK, X_OK, stat
from stat import S_IROTH, S_IWOTH, S_IXOTH
from os.path import join
from django.conf import settings


def test_write_allowed():
	"""
		Test if directories that should be writable are indeed so.
	"""
	for dr in [settings.MEDIA_ROOT,] + list(settings.LOCALE_PATHS):
		assert access(dr, W_OK | X_OK), 'directory "{0:s}" should be writable, but it is not'.format(dr)


def test_write_denied():
	"""
		If DEBUG is False (e.g. live server), check that the file permissions are sufficiently restrictive.
	"""
	if settings.DEBUG:
		return
	for dr in [settings.STATIC_ROOT, settings.BASE_DIR, join(settings.BASE_DIR, 'source')]:
		assert not access(dr, W_OK), 'directory "{0:s}" should be read-only, but it is not'.format(dr)


def test_settings_nonworld():
	"""
		Check that settings_local.py exists, is somewhat hidden and has a secret key and database settings.
	"""
	pth = join(settings.BASE_DIR, 'source', 'local.py')
	assert isfile(pth), 'you should have a local settings file with secret settings, located at "{0:s}"'.format(pth)
	mode = stat(pth).st_mode
	assert not mode & S_IROTH, 'local settings should not be world-readable (file "{0:s}")'.format(pth)
	assert not mode & S_IWOTH, 'local settings should not be world-writable (file "{0:s}")'.format(pth)
	assert not mode & S_IXOTH, 'local settings should not be world-executable (file "{0:s}")'.format(pth)
	# with open(pth, 'r') as fh:
	# 	txt = fh.read()
	# 	assert findall(r'^SECRET_KEY\s*=\s*', txt, flags = MULTILINE), 'local settings should set SECRET_KEY (file "{0:s}")'.format(pth)
	# 	assert findall(r'^DATABASES\s*=\s*', txt, flags = MULTILINE), 'local settings should set DATABASES (file "{0:s}")'.format(pth)


