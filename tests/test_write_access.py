
from genericpath import isfile
from os import access, W_OK, X_OK, stat
from re import findall, MULTILINE
from stat import S_IROTH, S_IWOTH, S_IXOTH
from os.path import join
from svsite.settings import DEBUG, DATA_DIR, BASE_DIR  # intentionally imported directly since DEBUG gets overwritten


def test_write_allowed():
	"""
		Test if directories that should be writable are indeed so.
	"""
	for dr in ['data', 'media',]:
		assert access(join(DATA_DIR, dr), W_OK | X_OK), 'directory "{0:s}" should be writable, but it is not'.format(join(DATA_DIR, dr))
	for dr in ['lang',]:
		assert access(join(BASE_DIR, dr), W_OK | X_OK), 'directory "{0:s}" should be writable, but it is not'.format(join(BASE_DIR, dr))


def test_write_denied():
	"""
		If DEBUG is False (e.g. live server), check that the file permissions are sufficiently restrictive.
	"""
	if DEBUG:
		return
	for dr in ['static',]:
		assert not access(join(DATA_DIR, dr), W_OK), 'directory "{0:s}" should be read-only, but it is not'.format(join(DATA_DIR, dr))
	for dr in ['source', 'dev', 'docs', 'tests',]:
		assert not access(join(BASE_DIR, dr), W_OK), 'directory "{0:s}" should be read-only, but it is not'.format(join(BASE_DIR, dr))


def test_settings_nonworld():
	"""
		Check that settings_local.py exists, is somewhat hidden and has a secret key and database settings.
	"""
	pth = join(BASE_DIR, 'source', 'svsite', 'settings_local.py')
	assert isfile(pth), 'you should have a local settings file with secret settings, located at "{0:s}"'.format(pth)
	mode = stat(pth).st_mode
	assert not mode & S_IROTH, 'local settings should not be world-readable (file "{0:s}")'.format(pth)
	assert not mode & S_IWOTH, 'local settings should not be world-writable (file "{0:s}")'.format(pth)
	assert not mode & S_IXOTH, 'local settings should not be world-executable (file "{0:s}")'.format(pth)
	with open(pth, 'r') as fh:
		txt = fh.read()
		assert findall(r'^SECRET_KEY\s*=\s*', txt, flags = MULTILINE), 'local settings should set SECRET_KEY (file "{0:s}")'.format(pth)
		assert findall(r'^DATABASES\s*=\s*', txt, flags = MULTILINE), 'local settings should set DATABASES (file "{0:s}")'.format(pth)


