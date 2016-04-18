
from os import devnull
from django.core.management import call_command
import sys


def test_templates_valid():
	"""
		Check templates based on django-extensions' validate_templates. Some magic with stdout because the stdout argument gets ignored.

		The `call_command` will raise an error when it fails, no need for asserts.
	"""
	null = open(devnull, 'a')
	stdout_backup, sys.stdout = sys.stdout, null
	call_command('validate_templates', '--break', '--check-urls', interactive = False, stdout = null)
	sys.stdout = stdout_backup


