from django.http import HttpResponse
from django.shortcuts import render_to_response
from django.template import RequestContext


# Create your views here.
def index(request):
    context = RequestContext(request)
    context_dict = {'boldmessage': "I am bold font from the context"}
    return render_to_response('rango/index.html', context_dict, context)


def about(request):
    return render_to_response('rango/about.html', {}, RequestContext(request))