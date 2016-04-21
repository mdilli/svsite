
from os import environ
from django.core.wsgi import get_wsgi_application
from os.path import abspath, dirname
from sys import path


path.insert(0, dirname(abspath(__file__)))

environ.setdefault("DJANGO_SETTINGS_MODULE", "settings")
# from http://security.stackexchange.com/questions/8964/trying-to-make-a-django-based-site-use-https-only-not-sure-if-its-secure
environ['HTTPS'] = 'on'
environ['wsgi.url_scheme'] = 'https'

application = get_wsgi_application()


