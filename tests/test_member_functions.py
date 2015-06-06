
from member.functions import email_to_name


def test_email_to_name():
	assert email_to_name('alpha..beta+test@domain.sub.ext') == 'Alpha Beta'


