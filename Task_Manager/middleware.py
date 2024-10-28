class DisableCSRFMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        response = self.get_response(request)
        return response

    def process_view(self, request, callback, callback_args, callback_kwargs):
        if request.path.startswith("/admin/"):
            return None
        setattr(request, "_dont_enforce_csrf_checks", True)
        return None
