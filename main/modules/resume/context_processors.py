"""
    Resume context processors
    =========================

    This module defines context processors related to the resume website.

"""

from flask import current_app


def google_metadata():
    """ Inserts a Google site verification code into the context. """
    return {
        'google_site_verification_code': current_app.config.get('GOOGLE_SITE_VERIFICATION_CODE'),
    }
