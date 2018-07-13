from django.urls import reverse
from django.utils.http import is_safe_url


def get_redirect_link(request):
    redirect_to = request.POST.get('next', request.META.get('HTTP_REFERER'))

    if redirect_to == request.path:
        redirect_to = reverse('index-view')

    url_is_safe = is_safe_url(
        url=redirect_to,
        allowed_hosts=request.get_host(),
        require_https=request.is_secure(),
    )

    return redirect_to if url_is_safe else reverse('index-view')
