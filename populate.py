# Setup the Django environment so we can access our models
import os
import datetime
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "PollApp.settings")

from polls.models import *
from django.utils import timezone

poll_questions = ['What is your favorite type of music',
				  'What\'s your favorite cartoon',
				  'Enjoying Django',
				  'Is schodinger\'s cat still alive',
				  'Do you trust atoms']

poll_choices = [['Classical', 'Pop', 'Rock', 'Rap', 'Hip-hop', 'Metal', 'Country', 'Who cares?'],
				['The Simpsons', 'Spongebob Squarepants', 'Family Guy', 'South Park', 'Avatar - The last Airbender', 'ALL of \'em!', 'Some other cartoon', 'None, cartoons are for DORKS!'],
				['Na! Its too boring', 'Eh, its ok ...', 'Hell Yeah! Its so awesome and easy'],
				['Yes', 'No', 'Maybe'],
				['Sure, what\'s not to trust?', 'No way! They make up everything.']]

now = timezone.now()

def main():
	for i in range(len(poll_questions)):
		p = Poll(question=poll_questions[i], pubdate=now)
		p.save()
		print 'Added poll - %s' % poll_questions[i]
		for j in range(len(poll_choices[i])):
			c = Choice(poll=p, choice_text=poll_choices[i][j], votes=0)
			c.save()
			print '\tAdded choice - %s' % poll_choices[i][j]


if __name__ == '__main__':
	main()