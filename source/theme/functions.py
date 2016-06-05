
from django.conf import settings
from functools import lru_cache
from os import listdir
from os.path import join, exists, basename
from theme.classes import Theme


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


