from django.http import *
from django.core.cache import cache
from django.shortcuts import render_to_response
from django.conf import settings


from dreque_frontend.utils import render
from dreque import Dreque, DrequeWorker

REDIS_ADDR = getattr(settings, 'REDIS_ADDR', '127.0.0.1')

def overview(request):
    dreque = Dreque(REDIS_ADDR)
    worker = DrequeWorker('', REDIS_ADDR)
    return render(request, 'dreque_frontend/overview.html', {'dreque': dreque, 'worker': worker})

def queue_detail(request, queue_name):
    dreque = Dreque(REDIS_ADDR)
    return render(request, 'dreque_frontend/queue.html', {'queue_name': queue_name, 'dreque': dreque})