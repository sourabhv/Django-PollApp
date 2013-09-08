import datetime

from django.utils import timezone
from django.test import TestCase
from django.core.urlresolvers import reverse

from polls.models import Poll

class PollMethodTests(TestCase):
	def test_wasPublishedRecently_with_future_poll(self):
		'''
		wasPublishedRecently() should return False for polls whose
		pub_date is in the future
		'''
		future_poll = Poll(pubdate=timezone.now() + datetime.timedelta(days=30))
		self.assertEqual(future_poll.wasPublishedRecently(), False)

	def test_wasPublishedRecently_with_recent_poll(self):
		'''
		wasPublishedRecently() should return True for polls which
		are recent published
		'''
		future_poll = Poll(pubdate=timezone.now() - datetime.timedelta(hours=3))
		self.assertEqual(future_poll.wasPublishedRecently(), True)

	def test_wasPublishedRecently_with_old_poll(self):
		'''
		wasPublishedRecently() should return False for polls which
		are old
		'''
		future_poll = Poll(pubdate=timezone.now() - datetime.timedelta(hours=30))
		self.assertEqual(future_poll.wasPublishedRecently(), False)

def create_poll(question, days):
	'''
	Creates a poll with the given 'question' published the given number of
	'days' offset to now (negative for polls published in the past,
	positive for polls that have yet to be published).
	'''
	return Poll.objects.create(question=question, pubdate=timezone.now()+datetime.timedelta(days=days))

class PollViewTest(TestCase):
	def test_index_view_with_no_polls(self):
		'''
		If no polls are available then an appropriate message should be displayed
		'''
		response = self.client.get(reverse('polls:index'))
		self.assertEqual(response.status_code, 200)
		self.assertContains(response, "No polls available")
		self.assertQuerysetEqual(response.context['latest_polls'], [])

	def test_index_view_with_a_past_poll(self):
		'''
		Polls with a pub_date in the past should be displayed on the index page.
		'''
		create_poll(question='Past poll', days=-30)
		response = self.client.get(reverse('polls:index'))
		self.assertQuerysetEqual(
			response.context['latest_polls'], ['<Poll: Past poll>']
		)

	def test_index_view_with_a_future_poll(self):
		'''
		Polls with a pub_date in the future should not be displayed on the
		index page.
		'''
		create_poll(question='Future poll', days=30)
		response = self.client.get(reverse('polls:index'))
		self.assertContains(response, 'No polls available', status_code=200)
		self.assertQuerysetEqual(response.context['latest_polls'], [])

	def test_index_view_with_a_past_poll_and_a_future_poll(self):
		'''
		Even if both past and future polls exist, only past polls should be
		displayed.
		'''
		create_poll(question='Future poll', days=30)
		create_poll(question='Past poll', days=-30)
		response = self.client.get(reverse('polls:index'))
		self.assertEqual(response.status_code, 200)
		self.assertQuerysetEqual(
			response.context['latest_polls'], ['<Poll: Past poll>']
		)

	def test_index_view_with_two_past_polls(self):
		'''
		The polls index page may display multiple polls.
		'''
		create_poll(question='Past poll 1', days=-15)
		create_poll(question='Past poll 2', days=-30)
		response = self.client.get(reverse('polls:index'))
		self.assertEqual(response.status_code, 200)
		self.assertQuerysetEqual(
			response.context['latest_polls'], ['<Poll: Past poll 1>', '<Poll: Past poll 2>']
		)
