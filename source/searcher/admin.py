
from cms.admin.placeholderadmin import PlaceholderAdminMixin
from django.contrib import admin
from hvad.admin import TranslatableAdmin
from searcher.models import SearchResults


class MultilingualModelAdmin(TranslatableAdmin, PlaceholderAdminMixin, admin.ModelAdmin):
	pass


admin.site.register(SearchResults, MultilingualModelAdmin)



# superuser_admin = SuperuserAdminSite(name='superuser')
# census_admin = CensusAdminSite(name='census')


