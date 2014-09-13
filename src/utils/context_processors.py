# -*- coding: utf-8 -*-

# Standard library imports
# Third party imports
from django.conf import settings
from django.contrib.sites.models import Site

# Local application / specific library imports


def site(request):
    return {
        'site': Site.objects.get_current()
    }


def canonical_url(request):
    current_site = Site.objects.get_current()
    path = request.get_full_path()
    path_clean = path.replace('/', '')

    if request.LANGUAGE_CODE:
        lang_code = request.LANGUAGE_CODE
    else:
        lang_code = settings.LANGUAGE_CODE

    if lang_code in request.get_full_path().split('/'):
        url = 'http://' + current_site.domain + request.get_full_path()
    else:
        url = 'http://' + current_site.domain + '/' + lang_code + request.get_full_path()

    if hasattr(settings, 'URLS_WITHOUT_LANGUAGE_REDIRECT'):
        for exclude_path in settings.URLS_WITHOUT_LANGUAGE_REDIRECT:
            if exclude_path in path_clean:
                url = 'http://' + current_site.domain + path

    return {
        'canonical_url': url
    }
