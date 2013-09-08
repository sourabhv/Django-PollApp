import datetime

from django.db import models
from django.utils import timezone

class Poll(models.Model):
	question = models.CharField(max_length=200)
	pubdate = models.DateTimeField(verbose_name=u'publication date', default=timezone.now())

	def wasPublishedRecently(self):
		now = timezone.now()
		return now - datetime.timedelta(days=1) <= self.pubdate < now
	wasPublishedRecently.boolean = True
	wasPublishedRecently.short_description = 'Published recently?'
	wasPublishedRecently.admin_order_field = 'pubdate'

	def __unicode__(self):
		return self.question

class Choice(models.Model):
	poll = models.ForeignKey(Poll)
	choice_text = models.CharField(max_length=200)
	votes  = models.IntegerField(default=0)
	def __unicode__(self):
		return self.choice_text
