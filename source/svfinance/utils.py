
from django.core.validators import RegexValidator, MinLengthValidator, MaxLengthValidator
from django.utils.timezone import now
from re import sub


class InvalidCodeException(Exception):
	pass


CODE_VALIDATORS = [
	RegexValidator(r'[A-Z]', 'Capital letters are not allowed.', inverse_match=True),
	RegexValidator(r'__', 'Repeated underscores are not allowed.', inverse_match=True),
	RegexValidator(r'^[a-z0-9_]+$', 'The value can only contain letters, numbers and underscores.'),
	RegexValidator('^[a-z].*[a-z0-9]$', 'The value should start with a letter and end in a letter or number.'),
	RegexValidator(r'[a-z0-9_]', 'Only letters, numbers and underscores are allowed'),
	MinLengthValidator(2, 'The minimum length is 2.'),
	MaxLengthValidator(48, 'The maximum length is 48.'),
]


def to_code(name, check=True):
	"""
	Attempt to convert name to code. Raises an error if it fails.
	"""
	code = name.lower()
	code = sub(r'[\s\-+]', '_', code)
	code = sub(r'[^a-z0-9_]', '', code)
	code = sub(r'__+', '_', code)
	code = sub(r'^[0-9_]+', '', code)
	code = sub(r'_+$', '', code)
	if check:
		assert 2 <= len(code) <= 48, 'Length should be between 2 and 48.'
	return code


def today():
	return now().date()


