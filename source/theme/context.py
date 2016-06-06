
from logging import warning
from django.conf import settings
from theme.functions import get_themes


def theme_context(request):
	themes = get_themes()
	if request.user.is_authenticated():
		if request.user.theme in themes:
			theme = themes[request.user.theme]
		else:
			if request.user.theme is not None:
				warning('user {0:s} has invalid theme {1:s} set')
			theme = themes[settings.SV_DEFAULT_THEME]
	else:
		theme = themes[settings.SV_DEFAULT_THEME]
	return {
		'THEME': theme,
		'THEME_PREFIX': theme.prefix(),
		'THEME_BASE': theme.relative_template_path(),
		'THEME_HEAD': theme.relative_template_head_path(),
		'SITE_DISP_NAME': settings.SITE_DISP_NAME,
	}



