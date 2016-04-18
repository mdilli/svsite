
from os import devnull
from pytest import mark
from django.core.management import call_command
import sys


@mark.django_db
def test_cms_check():
	"""
		Test django-cms with it's build-in command `cms check`.

		The `call_command` will raise an error when it fails, no need for asserts.
	"""
	with open(devnull, 'a') as null:
		stdout_backup, sys.stdout = sys.stdout, null
		call_command('cms', 'check', interactive = False, stdout = null)
		sys.stdout = stdout_backup


