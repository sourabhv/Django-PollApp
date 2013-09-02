from django.contrib import admin
from polls.models import *

class ChoiceInline(admin.TabularInline):
	model = Choice
	extra = 3

class PollAdmin(admin.ModelAdmin):
	fields = ('question', 'pubdate')
	readonly_fields = ('pubdate',)
	list_display = ('question', 'pubdate', 'wasPublishedRecently')
	list_filter = ('pubdate',)
	search_fields = ('question',)
	inlines = [ChoiceInline]
	data_hierarchy = 'pubdate'

admin.site.register(Poll, PollAdmin)
# admin.site.register(Choice)