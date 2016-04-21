
from svfinance.utils import to_code


def test_to_code():
	assert to_code('Hello World') == 'hello_world'
	assert to_code('Hello  -World') == 'hello_world'
	assert to_code('9 HeLLo') == 'hello'
	assert to_code('HeLLo+') == 'hello'
	assert to_code('!@h#$%-^&*i()') == 'h_i'


