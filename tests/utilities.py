
from bs4 import BeautifulSoup
from django.contrib.auth import get_user_model


def create_user():
	user = get_user_model()(email = 'test@domain.ext')
	user.set_password('test')
	user.save()
	return user


def get_form_errors(html):
	# only tested for nonfield errors! extend when needed
	soup = BeautifulSoup(html)
	error_tags = soup.find_all(attrs = {'class': 'errorlist'})[0]
	errors = [tag.contents[0] for tag in error_tags.contents]
	return '; '.join(errors)

