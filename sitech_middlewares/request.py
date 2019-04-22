from threading import local

_thread_locals = local()


class RequestViewMiddleware:
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
    try:
        return _thread_locals.request
    except AttributeError:
        return None