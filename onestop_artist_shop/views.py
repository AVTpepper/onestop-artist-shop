from django.views.defaults import permission_denied
from django.shortcuts import render


def bad_request(request, exception=None):
    """
    Render a custom 400 Bad Request error page.
    """
    return render(request, 'errors/400.html', status=400)


def permission_denied(request, exception=None):
    """
    Render a custom 403 Permission Denied error page.
    """
    return render(request, 'errors/403.html', status=403)


def page_not_found(request, exception=None):
    """
    Render a custom 404 Page Not Found error page.
    """
    return render(request, 'errors/404.html', status=404)


def server_error(request, exception=None):
    """
    Render a custom 500 Server Error page.
    """
    return render(request, 'errors/500.html', status=500)