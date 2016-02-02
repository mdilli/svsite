#!/usr/bin/env python

from os import environ
from os.path import abspath, dirname
from sys import path, argv


if __name__ == '__main__':
	path.insert(0, dirname(abspath(__file__)))
	environ.setdefault("DJANGO_SETTINGS_MODULE", "settings")
	from django.core.management import execute_from_command_line
	execute_from_command_line(argv)


