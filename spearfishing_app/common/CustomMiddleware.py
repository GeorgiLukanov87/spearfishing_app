from django.http import HttpResponseServerError
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
