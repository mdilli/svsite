
from django.contrib.auth import get_user_model
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404


@login_required
def member_profile_me(request):
	print('user model:', type(request.user))
	return redirect(to = request.user)


def member_profile(request, pk, label = None):
	user = get_object_or_404(klass = get_user_model(), pk = pk)
	return render(request, 'member_profile.html', {
		'user': user,
	})


