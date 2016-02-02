
from django.http import HttpResponse
from django.middleware.csrf import get_token
from django.shortcuts import render
from badges.badges import BADGE_HASHMAP, BADGE_KEYMAP
from badges.management.commands.badge_hash import make_hash
from badges.models import BadgeAward


def badge_win(request):
	if not request.user.is_authenticated():
		return HttpResponse('not logged in', status=401)
	if not 'b' in request.GET:
		return HttpResponse('no "b" GET parameter (badge)', status=422)
	if not 'c' in request.GET:
		return HttpResponse('no "c" GET parameter (auth)', status=422)
	if not request.GET['c'] == get_token(request):
		return HttpResponse('invalid "c" GET parameter', status=403)
	hash = make_hash(request.GET['b'])
	if hash in BADGE_HASHMAP:
		badge = BADGE_HASHMAP[hash]
		if not BadgeAward.objects.filter(user=request.user, badge=badge.key):
			award = BadgeAward(user=request.user, badge=badge.key)
			award.save()
			return HttpResponse('you won swott!', status=200)
		return HttpResponse('you already have this badge', status=410)


#todo: turn into cms plugin
def badge_info(request):
	badge_key = 'soatt'
	if not badge_key in BADGE_KEYMAP:
		return HttpResponse('no')  # todo notification('There is no badge with name "{0:s}"'.format(badge_name)
	badge = BADGE_KEYMAP[badge_key]
	return render(request, 'badge_info.html', {
		'badge': badge,
	})


