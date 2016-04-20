
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


with open('dev/requires.pip', 'r') as fh:
	requirements = list(req.strip() for req in fh.read().splitlines())
	requirements = list(req.split('#')[0] for req in requirements if (req and not req.startswith('#')))


setup(
	name='base',
	description='reusable association website',
	url='https://github.com/mverleg/svsite',
	version=open(join('dev', 'VERSION')).read().strip(),
	packages=['', 'base'], #find_packages()
	#package_dir={'': 'source'},
	package_data={
		'docs': 'docs',
		'tests': 'tests',
	},
	test_suite='tests',
	license='BSD License',
	author='Mark, ...',
	author_email='markv.nl.dev@gmail.com',
	install_requires=requirements, # see documentation for non-pip requirements
	classifiers=[
		'Development Status :: 2 - Pre-Alpha',
		'Intended Audience :: Developers',
		'License :: OSI Approved :: BSD License',
		'Programming Language :: Python :: 3.4',
		'Framework :: Django :: 1.9',
		'Environment :: Web Environment',
		'Do Not Upload By Accident',
	],
	cmdclass = {'test': PyTest},  #todo add a comment what this does and why it's a good idea...
)


