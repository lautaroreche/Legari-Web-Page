from django.http import HttpResponsePermanentRedirect

class WWWRedirectMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        host = request.get_host()
        if host.startswith("fabianlegari.com"):
            new_url = request.build_absolute_uri().replace("//fabianlegari.com", "//www.fabianlegari.com", 1)
            return HttpResponsePermanentRedirect(new_url)
        return self.get_response(request)
