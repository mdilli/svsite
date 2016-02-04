
from django.conf import settings
from django.contrib.auth import get_user_model
from django.contrib.auth.decorators import login_required
from django.core.urlresolvers import reverse
from django.shortcuts import render, redirect, get_object_or_404


@login_required
def member_profile_me(request):
	print('user model:', type(request.user))
	return redirect(to = request.user)


def member_profile(request, pk=None, label=None):
	if pk is None:
		if not request.user.is_authenticated:
			return redirect(settings.LOGIN_URL)
		return redirect(reverse('profile_info', kwargs=dict(pk=request.user.pk, label=request.user.slug)))
	user = get_object_or_404(klass = get_user_model(), pk = pk)
	return render(request, 'member_profile.html', {
		'user': user,
	})


