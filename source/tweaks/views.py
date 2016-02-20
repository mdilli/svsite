
from base.views import render_cms_special


def display_exception(request, err, template, **kwargs):
	context = dict(
		exception=err,
		caption=err.caption,
		message=err.message,
		next=err.next,
		EXCEPTION_BASE_TEMPLATE=template,
	)
	context.update(err.context)
	response = render_cms_special(request, err.template, context)
	response.status_code = err.status_code
	return response


