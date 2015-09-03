
"""
	Install svSite and dependencies.

	Tests based on https://pytest.org/latest/goodpractises.html .
"""

from distutils.core import setup, Command
from os.path import join


class PyTest(Command):
	user_options = []

	def initialize_options(self):
		pass

	def finalize_options(self):
		pass

	def run(self):
		from subprocess import call
		from sys import executable
		errno = call([executable, 'tests/runtests.py', 'tests'])
		raise SystemExit(errno)


with open('dev/requirements.pip', 'r') as fh:
	requirements = fh.read().splitlines()


setup(
	name='svsite',
	version=open(join('dev', 'VERSION')).read().strip(),
	packages=['', 'svsite'],
	package_dir={'': 'source'},
	package_data={
		'docs': 'docs',
		'static': 'static',
	},
	test_suite='tests',
	url='https://github.com/mverleg/svsite',
	license='MIT License',
	author='mark, ...',
	author_email='contact me on github',
	description='reusable association website',
	install_requires=requirements, # see documentation for non-pip requirements
	classifiers=[
		'Development Status :: 2 - Pre-Alpha',
		'Intended Audience :: Developers',
		'License :: OSI Approved :: MIT License',
		'Programming Language :: Python :: 3.4',
		'Framework :: Django :: 1.8',
		'Environment :: Web Environment',
	],
	cmdclass = {'test': PyTest},
)


