from threading import local

from django.contrib.auth.models import AnonymousUser

_thread_locals = local()


class RequestMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        _thread_locals.request = request
        try:
            return self.get_response(request)
        finally:
            del _thread_locals.request
        return self.get_response(request)


def get_current_request():
    """
    Gets the request.
    :return: Django request object
    """
    try:
        return _thread_locals.request
    except AttributeError:
        return None


def get_current_user():
    """
    Gets the current user from the current request. In case there is no current
    request, or there is no user information attached to the request, an AnonymousUser object
    is returned.
    :return: User object
    """
    request = get_current_request()
    if not request or not hasattr(request, 'user'):
        return AnonymousUser()
    return request.user
