
from display_exceptions import NotFound, PermissionDenied
from django.conf import settings
from django.contrib.auth import get_user_model
from django.contrib.auth.decorators import login_required
from django.core.urlresolvers import reverse
from django.db.models import When, Case
from django.db.models.functions import Value, Concat
from django.shortcuts import redirect
from base.views import render_cms_special


# @login_required
from member.models import Team


def team_info_all(request):
	teams = Team.objects.filter(listed=True).order_by('name')
	return render_cms_special(request, 'team_info_all.html', dict(
		teams=teams,
	))


def team_info(request, slug):
	try:
		team = Team.objects.get(slug=slug)
	except Team.DoesNotExist:
		raise NotFound(message='No team with {0:} found.'.format(slug), caption='Team not found', next=reverse('team_info_all'))
	if team.listed is False:
		if not request.user.is_authenticated():
			raise PermissionDenied(message='Team {0:} is not visible if you\'re not logged in.'
				.format(team), next=reverse('account_login'))
		if not request.user.pk in set(member.pk for member in team.roles):
			raise PermissionDenied(message='Team {0:} is not visible to you (only admins can view it).'
				.format(team), next=reverse('team_info_all'))
	return render_cms_special(request, 'team_info.html', dict(
		team=team,
	))


@login_required
def member_profile_me(request):
	return redirect(to=request.user)


@login_required
def member_profile_all(request):
	"""
	Members are sorted by full name (first + last), with empty names after full ones.
	"""
	users = get_user_model().objects.filter(is_active=True).annotate(name_null=Case(
		When(first_name='', last_name='', then=Value('1')),
		default=Concat(Value('0'), 'first_name', Value(' '), 'last_name')
	)).order_by('name_null')
	return render_cms_special(request, 'member_profile_all.html', dict(
		users=users,
	))


def member_profile(request, pk=None, label=None):
	#todo: cms update title
	if pk is None:
		if not request.user.is_authenticated:
			return '{0:s}?next={1:s}'.format(redirect(settings.LOGIN_URL), request.path)
		return redirect(reverse('profile_info', kwargs=dict(pk=request.user.pk, label=request.user.slug)))
	try:
		user = get_user_model().objects.get(pk=pk)
	except get_user_model().DoesNotExist:
		raise NotFound(message='No user with key {0:} found.'.format(pk), caption='User not found', next=reverse('profile_info_all'))
	return render_cms_special(request, 'member_profile.html', dict(
		user=user,
	))


