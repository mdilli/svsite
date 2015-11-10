
from django.core.urlresolvers import reverse
from django.shortcuts import redirect
from django.utils.timezone import now
from django.views.generic import DetailView, ListView
from activity.models import Activity


def to_activity_overview(request):
	return redirect(to = reverse('activity_overview'))


class ActivityOverview(ListView):

	#todo: no class views, they suck
	template_name = 'activity_overview.html'

	def get_queryset(self):
		return Activity.objects.filter(end__gt = now())


class ActivityInfo(DetailView):

	model = Activity
	template_name = 'activity_info.html'

	# def get_object should already work


