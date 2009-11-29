from django.http import *
from django.core.cache import cache
from django.shortcuts import render_to_response

from dreque_frontend.utils import render
from dreque import Dreque, DrequeWorker


def overview(request):
    dreque = Dreque("127.0.0.1")
    worker = DrequeWorker('', "127.0.0.1")
    return render(request, 'dreque_frontend/overview.html', {'dreque': dreque, 'worker': worker})

def queue_detail(request, queue_name):
    dreque = Dreque("127.0.0.1")
    return render(request, 'dreque_frontend/queue.html', {'queue_name': queue_name, 'dreque': dreque})