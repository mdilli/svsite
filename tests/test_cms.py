
from os import devnull
from django.core.management import call_command
import sys


def test_cms_check():
	"""
		Test django-cms with it's build it command `cms check`.

		The `call_command` will raise an error when it fails, no need for asserts.
	"""
	null = open(devnull, 'a')
	stdout_backup, sys.stdout = sys.stdout, null
	call_command('cms', 'check', interactive = False, stdout = null)
	sys.stdout = stdout_backup


