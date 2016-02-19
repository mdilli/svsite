
from cms.models import PlaceholderField, CMSPlugin
from cms.plugin_rendering import render_plugin
from django.conf import settings
from django.db.models import CharField
from hvad.manager import TranslationManager, FallbackQueryset
from hvad.models import TranslatableModel, TranslatedFields


class MyFallbackQueryset(FallbackQueryset):
	translation_fallbacks = (None,) + tuple(v[0] for v in settings.LANGUAGES)


class SearchResults(TranslatableModel):
	translations = TranslatedFields(
		title=CharField(max_length=64),
	)
	placeholder = PlaceholderField('search_results')

	objects = TranslationManager(default_class=MyFallbackQueryset)

	class Meta:
		verbose_name = 'Search result'
		verbose_name_plural = 'Search results'

	template = 'search_results.html'

	def __str__(self):
		return self.title

	def render_plugin(self, context=None, placeholder=None, admin=False, processors=None):
		return render_plugin(context=context, instance=self, placeholder=placeholder, template=self.template,
			processors=processors)


