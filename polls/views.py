from django.http import Http404, HttpResponse, HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.core.urlresolvers import reverse
from django.utils import timezone

from polls.models import *

def index(request):
	latest_polls = Poll.objects.filter(pubdate__lte=timezone.now()).order_by('-pubdate')[:10]
	return render(request, 'polls/index.html', {'latest_polls': latest_polls})

def detail(request, poll_id):
	poll = get_object_or_404(Poll, pk=poll_id)
	return render(request, 'polls/detail.html', {'poll': poll})

def vote(request, poll_id):
	if request.method == 'POST':
		poll = get_object_or_404(Poll, pk=poll_id)
		try:
			choice = poll.choice_set.get(pk=request.POST['choice'])
		except (KeyError, Choice.DoesNotExist):
			return render(request, 'polls/detail.html', {
				'poll': poll,
				'error_message': 'No choice was selected',
			})
		else:
			choice.votes += 1
			choice.save()
			return HttpResponseRedirect(reverse('polls:result', args=(poll.id,)))
	else:
		return HttpResponseRedirect(reverse('polls:index'))

# def vote(request, poll_id, choice_id):
# 	poll = get_object_or_404(Poll, pk=poll_id)
# 	choice = get_object_or_404(Choice, pk=choice_id)
# 	if choice not in poll.choice_set.all():
# 		raise Http404
# 	else:

def result(request, poll_id):
	poll = get_object_or_404(Poll, pk=poll_id)
	return render(request, 'polls/result.html', {'poll': poll})