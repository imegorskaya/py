# Create your views here.
from django.shortcuts import render_to_response
from django.http import Http404
from polls.models import Poll


def index(request,poll_id):
    try:
        p = Poll.objects.get(pk=poll_id)
    except Poll.DoesNotExist:
        raise Http404
#    return render_to_response('index.html')
    return render_to_response('index.html', {'poll_list': p})


def detail(request, poll_id):
    try:
        p = Poll.objects.get(pk=poll_id)
    except Poll.DoesNotExist:
        raise Http404
    return render_to_response('detail.html', {'poll_list': p})


def results(request, poll_id):

    return render_to_response('results.html')


def vote(request, poll_id):
    return render_to_response('vote.html')

