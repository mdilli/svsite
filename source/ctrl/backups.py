
from datetime import datetime
from io import StringIO
from django.contrib.auth.decorators import login_required
from django.contrib.sites.shortcuts import get_current_site
from django.core.management import call_command
from django.http import FileResponse, HttpResponseForbidden


@login_required
def download_database(request):
	"""
		Make a json dump of the entire database excluding sessions.
	"""
	if not request.user.has_permission_superuser:
		return HttpResponseForbidden('you do not have permission to create backups')
	data = StringIO()
	call_command('dumpdata', exclude = ['sessions.session'], natural_foreign = True, natural_primary = True, stdout = data)
	response = FileResponse(data.getvalue(), content_type = 'application/json')
	response['Content-Disposition'] = "attachment; filename={0:s}_{1:s}.json".format(
		get_current_site(request).domain, datetime.now().strftime('%Y%b%d').lower())
	return response


@login_required
def upload_database(request):
	"""
		Upload a json dump as exported by download_database, and overwrite the database with it.
	"""
	if not request.user.has_permission_superuser:
		return HttpResponseForbidden('you do not have permission to create backups')
	raise NotImplementedError('upload database')
	# todo issue #18


