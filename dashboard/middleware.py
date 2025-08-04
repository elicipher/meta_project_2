from django.http import Http404

class DashboardAccessMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        path = request.path
        if path.startswith('/dashboard/'):
            if not request.user.is_authenticated or not (request.user.is_admin or request.user.is_superuser):
                raise Http404("شما اجازه دسترسی به این بخش را ندارید.")
        return self.get_response(request)