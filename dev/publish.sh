#!/usr/bin/env bash

# run tests with py.test
py.test tests || exit 10

# check style with pylint, exit for any problem except convention messages
#pylint source
#if [ "$?" -ne 16 ]; then exit 20; fi

# create a file to run tests without needing py.test (or plugins)
py.test --genscript=tests/runtests.py || exit 30

# create sphix documentation
cd docs && make dirhtml && cd .. || exit 40

# the user should not forget to update the version number, and create a tag in git
printf "\nThe current version is: %s\n" "$(cat 'dev/VERSION')"
printf "Do not forget to increment it, and add a git tag\n"


