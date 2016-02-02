
from os import listdir
from re import match
from django.conf import settings
from functools import lru_cache
from os.path import join, exists, basename


class Theme:
	"""
	A theme consists of these directories:

	- templates/  - required, and should contain base.html (optionally head.html)
	- static/     - any static files, if desired
	- info/       - optional extra files, for example:
		readme.rst
		description.rst
		credits.rst
		license.txt

	Note that the split into head and body is necessary because sekizai requires
	the css and js blocks
	"""
	def __init__(self, name):
		assert match(r'^[a-zA-Z][a-zA-Z0-9\.\-,_]+$', name), \
			'Theme names should contain only letters, numbers and "_-+,." (got "{0:s}")'.format(name)
		self.base_template = join(settings.SV_THEMES_DIR, 'templates', name, 'base.html')
		assert exists(self.base_template), 'theme {0:s}: can\'t find "{1:s}"'.format(name, self.base_template)
		self.readme = self.description = self.credits = self.license = None
		self.name = name
		self.load()

	def load(self):
		self.load_info()

	def load_info(self):
		info_files = ('readme.rst', 'description.rst', 'credits.rst', 'license.txt')
		info_path = join(settings.SV_THEMES_DIR, 'info', self.name)
		for info_file in info_files:
			attr_name = info_file.rsplit('.', maxsplit=1)[0]
			setattr(self, attr_name, None)
			if exists(join(info_path, info_file)):
				with open(join(info_path, info_file), 'r') as fh:
					setattr(self, attr_name, fh.read())

	def prefix(self):
		return self.name

	def relative_template_head_path(self):
		if exists(join(settings.SV_THEMES_DIR, 'templates', self.name, 'head.html')):
			return '{0:s}/{1:s}'.format(self.name, 'head.html')
		return 'default_head.html'

	def relative_template_path(self):
		return '{0:s}/{1:s}'.format(self.name, 'base.html')


@lru_cache(maxsize=None)
def get_themes():
	themes = {}
	for name in listdir(join(settings.SV_THEMES_DIR, 'templates')):
		if exists(join(settings.SV_THEMES_DIR, 'templates', name, 'base.html')):
			themes[name] = Theme(name)
		else:
			print('"{0:s}" not a valid template (not a directory containing base.html)'.format(name))
	assert settings.SV_DEFAULT_THEME in themes, 'SV_DEFAULT_THEME = "{0:s}" not found in SV_THEMES_DIR; found [{1:s}]'\
		.format(settings.SV_DEFAULT_THEME, ', '.join(basename(pth) for pth in themes.keys()))
	return themes


