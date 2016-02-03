#!/usr/bin/env bash

site_pack_path="$(python -c 'from distutils.sysconfig import get_python_lib; print(get_python_lib())')"
dev_dir="$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )"

cd "$site_pack_path/django/contrib/auth"
if [ -n "$(grep 'models.ManyToManyField(Group,' models.py)" ]
then
	printf "patching models.py in $(pwd)\n"
	patch --silent < "$dev_dir/django_auth.patch"
else
	printf "models.py in $(pwd) seems already patched\n"
fi


