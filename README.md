# Dreque frontend
A Django-based application for monitoring the current state of your dreque ([dreque on GitHub](http://github.com/samuel/dreque)).
Currently very much in development.

## Requirements
- [dreque](http://github.com/samuel/dreque)
- Django 1.0 or later
- redis

## Installation
- Add 'dreque_frontend' (the subdirectory of this one) somewhere on PYTHONPATH, and add it to your project's INSTALLED_APPS
- Add `REDIS_ADDR` to your `settings.py`. This can be either a IP, hostname (Redis will fall back to the default port) or either  a string in the format `hostname:ip` or a tuple in the format ('hostname', 'ip').
- Add `(r'^dreque/', include('dreque_frontend.urls')),` to your project's `urls.py`
- Go to /dreque/ and see it in action.

## Screenshot
![Dreque main screen](http://cld.ly/19lh2)