
from badges.models import BadgeType


SOATT = BadgeType(
	key='soatt',
	name='The Sword of a Thousand Truths',
	description='Bestowed upon this user by the powers that be, for displaying a profound understanding of the universe.',
	score=10,
	image='soatt.png',
	hash='zX3znn0AVJVqtyVC3mREMw'
)

badge_list = [
	SOATT,
]

BADGE_HASHMAP = {badge.hash: badge for badge in badge_list}
BADGE_KEYMAP = {badge.key: badge for badge in badge_list}
BADGE_CHOICES = ((badge.key, badge.name) for badge in badge_list)


