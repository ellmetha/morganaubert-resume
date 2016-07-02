# -*- coding: utf-8 -*-

from django.conf import settings
from django.contrib.sites.models import Site


def canonical_url(request):
    current_site = Site.objects.get_current()

    if request.LANGUAGE_CODE:
        lang_code = request.LANGUAGE_CODE
    else:
        lang_code = settings.LANGUAGE_CODE

    if lang_code in request.get_full_path().split('/'):
        url = 'http://' + current_site.domain + request.get_full_path()
    else:
        url = 'http://' + current_site.domain + '/' + lang_code + request.get_full_path()

    return {
        'canonical_url': url
    }


def google_metadata(request):
    return {
        'google_site_verification_code': settings.GOOGLE_SITE_VERIFICATION_CODE,
    }


def webpack(request):
    return {
        'WEBPACK_DEV_SERVER_URL': getattr(settings, 'WEBPACK_DEV_SERVER_URL', ''),
    }
