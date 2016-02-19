
"""
Imported from __init__.py
"""

from cms.models import Page, Title, PlaceholderField
from django.core.cache import cache
from django.db.models import signals, CharField
from hvad.models import TranslatableModel, TranslatedFields


# class SearchResults(TranslatableModel):
# 	translations = TranslatedFields(
# 		title=CharField(max_length=64),
# 	)
# 	placeholder = PlaceholderField('search_results')


def refresh_menu_cache(sender, **kwargs):
	print(' refreshing menu cache')
	# menu_pool.clear()  # found online but doesn't work
	cache.clear()


signals.post_save.connect(refresh_menu_cache, sender=Page, dispatch_uid='cms_post_save_page')
signals.post_delete.connect(refresh_menu_cache, sender=Page, dispatch_uid='cms_post_delete_page')
signals.post_save.connect(refresh_menu_cache, sender=Title, dispatch_uid='cms_post_save_title')
signals.post_delete.connect(refresh_menu_cache, sender=Title, dispatch_uid='cms_post_delete_title')


