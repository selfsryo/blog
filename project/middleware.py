from django.http import HttpResponsePermanentRedirect
from django.utils.deprecation import MiddlewareMixin


class RedirectHostMiddleware(MiddlewareMixin):
    def process_request(self, request):
        host = request.get_host()

        if host and ("example.fly.dev" in host):
            my_domain = "example.com"
            redirect_url = "%s://%s%s" % (request.scheme, my_domain, request.get_full_path())
            return HttpResponsePermanentRedirect(redirect_url)
