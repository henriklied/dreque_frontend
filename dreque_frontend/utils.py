from django.shortcuts import render_to_response
from django.template import RequestContext

def render(request, template, d):
    return render_to_response(template, d, context_instance=RequestContext(request))