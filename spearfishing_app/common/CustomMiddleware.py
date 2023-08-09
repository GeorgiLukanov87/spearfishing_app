from django.http import HttpResponseServerError
from django.shortcuts import redirect
from django.template.loader import get_template
from django.template import RequestContext


class CustomErrorMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        response = self.get_response(request)
        if response.status_code >= 500:
            return self.handle_error(request, response)
        return response

    def handle_error(self, request, response):
        template = get_template('404.html')
        context = RequestContext(request, {'status_code': response.status_code})
        return HttpResponseServerError(template.render(context))


class NoAdminAccessForRegularUserMiddleware:

    def __init__(self, get_response):
        self.get_response = get_response

    def _middleware(self, request, *args, **kwargs):
        if request.path.startswith("/admin/") and (not request.user.is_authenticated or not request.user.is_staff):
            return redirect('index')

        return None

    def __call__(self, request, *args, **kwargs):
        response = self._middleware(request, *args, **kwargs)

        if response is None:
            response = self.get_response(request, *args, **kwargs)

        return response
