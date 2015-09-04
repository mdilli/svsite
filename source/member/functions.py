
def email_to_name(email):
	#todo: unused
	"""
		Convert an email address to a name by replacing special characters by spaces and title-casing the result.
	"""
	name = email.split('@')[0].split('+')[0]
	name = ''.join(letter if letter.isalnum() else ' ' for letter in name)
	name = ' '.join(name.split())
	return name.title()


