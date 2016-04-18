
from json import dumps
from collections import OrderedDict
from django.conf import settings
from django.contrib.auth import authenticate, get_user_model
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from base.views import render_cms_special
from member.models import Team


def api_view(func):
	def func_with_header(request, *args, **kwargs):
		if not getattr(settings, 'INTEGRATION_KEYS', None):
			return HttpResponse('integration key not set on the server; service cannot be used', status=501)
		if request.method != 'POST':
			return HttpResponse('send a POST request', status=405)
		if 'key' not in request.POST:
			return HttpResponse('your request does not include an integration key', status=400)
		if request.POST['key'].strip() not in settings.INTEGRATION_KEYS:
			return HttpResponse('incorrect key', status=403)
		data = func(request, *args, **kwargs)
		resp = HttpResponse(dumps(data, indent=2, sort_keys=False), content_type='application/json')
		resp['Allow'] = 'POST'
		return resp
	return func_with_header


def api_info(request):
	return render_cms_special(request, 'api_info.html', {
		'DOMAIN': settings.SITE_URL,
		'INTEGRATION_KEYS_COUNT': len(getattr(settings, 'INTEGRATION_KEYS', ())),
		'INTEGRATION_ALLOW_EMAIL': getattr(settings, 'INTEGRATION_ALLOW_EMAIL', None),
	})


@csrf_exempt
@api_view
def user_list_api(request):
	users = get_user_model().objects.filter(is_active=True)
	if 'email' in request.POST:
		if not getattr(settings, 'INTEGRATION_ALLOW_EMAIL', False):
			return HttpResponse('email listing is turned off on the server; service cannot be used', status=501)
		return OrderedDict((user.username, user.email) for user in users)
	return list(user.username for user in users)


@csrf_exempt
@api_view
def team_list_api(request):
	teams = Team.objects.filter(listed=True)
	return list(team.name for team in teams)


@csrf_exempt
@api_view
def user_details_api(request):
	if 'username' not in request.POST and 'password' not in request.POST:
		return HttpResponse('your request does not include `username` and `password`', status=400)
	user = authenticate(username=request.POST['username'], password=request.POST['password'])
	if not user:
		if not get_user_model().objects.filter(username=request.POST['username']):
			return HttpResponse('user `{0:s}` does not exist'.format(request.POST['username']), status=404)
		return HttpResponse('incorrect password', status=403)
	if not user.is_active:
		return HttpResponse('the account `{0:s}` has been disabled'.format(user.username), status=403)
	bday = None
	if user.birthday:
		bday = user.birthday.strftime('%Y-%m-%d')
	return OrderedDict((
		('username', user.username),
		('first_name', user.first_name),
		('last_name', user.last_name),
		('email', user.email),
		('birthday', bday),
		('teams', {role.team.name: role.title for role in user.role_throughs}),
	))


@csrf_exempt
@api_view
def team_details_api(request):
	if 'teamname' not in request.POST:
		return HttpResponse('your request does not include team `name`', status=400)
	try:
		team = Team.objects.get(name=request.POST['teamname'])
	except Team.DoesNotExist:
		return HttpResponse('team `{0:s}` does not exist'.format(request.POST['teamname']), status=404)
	return OrderedDict((
		('hidden', not team.listed),
		('teamname', team.name),
		('description', team.description),
		('leaders', [admin.username for admin in team.admins.all()]),
		('members', {role.member.username: role.title for role in team.role_throughs}),
	))


