import datetime

from django.db import models
from django.utils import timezone

class Poll(models.Model):
	question = models.CharField(max_length=200)
	pubdate = models.DateTimeField(verbose_name=u'publication date',auto_now_add=True)

	def wasPublishedRecently(self):
		return self.pubdate >= timezone.now() - datetime.timedelta(days=1)
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
