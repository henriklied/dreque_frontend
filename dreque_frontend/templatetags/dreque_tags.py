import datetime
from django.template import Library

register = Library()

@register.filter
def peek(dreque, queue):
    return dreque.peek(queue, 0, 200)

@register.filter
def size(dreque, queue):
    return dreque.size(queue)

@register.filter
def dictify(d):
    return dict(d).items()

@register.filter
def evaluate(i):
    try:
        return eval(i)
    except:
        return i

@register.filter
def from_timestamp(ts):
    try:
        return datetime.datetime.fromtimestamp(ts)
    except:
        return ts

@register.filter
def typeof(s):
    return type(s)

@register.filter
def none_or_list(l):
    return l or None

@register.filter
def working_on(worker, worker_id):
    return worker.redis.get(worker._redis_key("worker:"+worker_id))