
"""
	A test to see if the server can start succesfully and let a user login.
"""

from bs4 import BeautifulSoup
from pytest import mark
from django.core.urlresolvers import reverse
from requests import get
from tests.utilities import create_user, get_form_errors


def test_homepage(live_server):
	url = '{0:s}/'.format(live_server.url)
	resp = get(url)
	assert resp.status_code == 200, 'url "{0:s}" returned status {1:d}'.format(url, resp.status_code)


@mark.django_db
def test_login(client):
	"""
		Test whether a user can login, and by doing that whether the server starts and functions correctly.

		All arguments are provided by pytest-django:

		:param client: Run requests through the site internally (no actual requests, server can be off).
		:param admin_user:
	"""
	user = create_user()
	login_form = client.get(reverse('account_login'))
	soup = BeautifulSoup(login_form.content)
	csrf_field = soup.find_all(attrs = {'name': 'csrfmiddlewaretoken'})[0]
	csrf_token = csrf_field['value']
	login_response = client.post(reverse('account_login'), data = {
		'login': user.email,
		'password': 'test',
		'csrfmiddlewaretoken': csrf_token,
	})
	assert login_response.status_code == 302, 'login page didn\'t redirect after POST; login probably failed; "{0:s}"'.format(get_form_errors(login_response.content))


