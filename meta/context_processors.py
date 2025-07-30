from django.conf import settings

def static_path(request):
    return {"STATIC_PATH": settings.STATIC_URL}