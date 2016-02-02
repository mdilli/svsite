
import hashlib
from base64 import urlsafe_b64encode
from django.core.management.base import BaseCommand


def make_hash(input):
	data1 = bytes(input, 'ascii')
	hasher1, hasher2 = hashlib.md5(), hashlib.md5()
	hasher1.update(data1)
	data2 = hasher1.digest()
	hasher2.update(data2)
	data3 = hasher2.digest()
	return urlsafe_b64encode(data3).decode('ascii')[:-2]


class Command(BaseCommand):
	help = 'Creates hash for a badge password'

	def add_arguments(self, parser):
		parser.add_argument('badge_password', type=str)

	def handle(self, badge_password, *args, **options):
		print(make_hash(badge_password))


