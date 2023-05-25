from django.shortcuts import redirect

class AdminLoginMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        if not request.user.is_authenticated and request.path.startswith('/admin'):
            return redirect('admin:login')
        return self.get_response(request)
