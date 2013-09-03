from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
from polls.models import *

def index(request):
	latest_polls = Poll.objects.order_by('-pubdate')[:5]
	for i in range(len(latest_polls)):
		if latest_polls[i].question[-1] == '?':
			latest_polls[i].question == latest_polls[i].question[:-1]

	return render(request, 'polls/index.html', {'latest_polls': latest_polls})

def detail(request, poll_id):
	poll = get_object_or_404(Poll, pk=poll_id)
	return render(request, 'polls/detail.html', {'poll': poll})

def result(request, poll_id):
	return HttpResponse('At result page of poll %s.' % poll_id)

def vote(request, poll_id):
	return HttpResponse('At vote page of poll %s.' % poll_id)
