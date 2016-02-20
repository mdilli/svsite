
from display_exceptions import NotFound
from django.conf import settings
from django.contrib.auth import get_user_model
from django.contrib.auth.decorators import login_required
from django.core.urlresolvers import reverse
from django.shortcuts import redirect, get_object_or_404
from base.views import render_cms_special


@login_required
def member_profile_me(request):
	return redirect(to=request.user)


@login_required
def member_profile_all(request):
	users = get_user_model().objects.filter(is_active=True).order_by('username')
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
		get_user_model().objects.get(pk=pk)
	except get_user_model().DoesNotExist:
		raise NotFound(message='No user with key {0:} found.'.format(pk), caption='User not found', next=reverse('profile_info_all'))
	user = get_object_or_404(klass = get_user_model(), pk=pk)  # tddo: update to display exceptions
	return render_cms_special(request, 'member_profile.html', dict(
		user=user,
	))


