from django.conf import settings


def google_metadata(request):
    """ Inserts a Google site verification code into the context. """
    return {'google_site_verification_code': settings.GOOGLE_SITE_VERIFICATION_CODE, }


def webpack(request):
    """ Inserts a Webpack dev server URL into the context. """
    return {'WEBPACK_DEV_SERVER_URL': settings.WEBPACK_DEV_SERVER_URL, } \
        if settings.WEBPACK_DEV_SERVER_STARTED else {}
