
"""
	A test to see if the server can start successfully and let a user login.

	Note that being in test mode turns SSL off, so that is not tested.
"""

from django.conf import settings
from pytest import mark


@mark.django_db
def test_server_status(client):
	langs = list(lang[0] for lang in settings.LANGUAGES)
	for lang in langs:
		resp = client.get('/', follow=True, HTTP_ACCEPT_LANGUAGE='en')
		if resp.status_code != 200:
			raise Exception(('could not reach the main page; either the server doesn\'t start correctly, '
				'or it doesn\'t have a main page in language {0:}\nerror: {1:}').format(lang, resp.content))
		print('>>', resp.content)
	assert False




# def create_user():
# 	user = get_user_model()(email = 'test@domain.ext')
# 	user.set_password('test')
# 	user.save()
# 	return user
#
#
# def get_form_errors(html):
#	#only tested for nonfield errors! extend when needed
	# soup = BeautifulSoup(html)
	# error_tags = soup.find_all(attrs = {'class': 'errorlist'})[0]
	# errors = [tag.contents[0] for tag in error_tags.contents]
	# return '; '.join(errors)
#
#
# def test_homepage(live_server):
# 	assert not getattr(settings, 'PREPEND_WWW', False), 'cannot test homepage request if www is prepended, since that doesn\'t work for localhost (the server still might or might not work)'
# 	url = live_server.url + '/'
# 	resp = get(url, verify = False)
# 	assert resp.status_code == 200, 'url "{0:s}" returned status {1:d}'.format(url, resp.status_code)
#
#
# @mark.django_db
# def test_login(client):
# 	"""
# 		Test whether a user can login, and by doing that whether the server starts and functions correctly.
#
# 		All arguments are provided by pytest-django:
#
# 		:param client: Run requests through the site internally (no actual requests, server can be off).
# 		:param admin_user:
# 	"""
# 	user = create_user()
# 	login_form = client.get(reverse('account_login'))
# 	soup = BeautifulSoup(login_form.content)
# 	csrf_fields = soup.find_all(attrs = {'name': 'csrfmiddlewaretoken'})
# 	assert csrf_fields, 'no csrf token found (no valid form)\npage = {0:s}'.format(str(soup))
# 	csrf_token = csrf_fields[0]['value']
# 	login_response = client.post(reverse('account_login'), data = {
# 		'login': user.email,
# 		'password': 'test',
# 		'csrfmiddlewaretoken': csrf_token,
# 	})
# 	assert login_response.status_code == 302, 'login page didn\'t redirect after POST; login probably failed; "{0:s}"' \
# 		.format(get_form_errors(login_response.content))


