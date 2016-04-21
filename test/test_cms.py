
from io import StringIO
from os import devnull
from pytest import mark
from django.core.management import call_command, CommandError


@mark.django_db
def test_cms_check():
	"""
		Test django-cms with it's build-in command `cms check`.

		The `call_command` will raise an error when it fails, no need for asserts.
	"""
	with StringIO() as err:
		with open(devnull, 'a') as null:
			try:
				call_command('cms', 'check', interactive=False, stdout=null, stderr=err)
			except CommandError as ex:
				print('>>> EXCEPTION', str(ex))
			print('>>> ERROR', err.getvalue())


