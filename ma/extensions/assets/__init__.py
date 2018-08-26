"""
    The assets extension
    ====================

    This module defines context processors and views that are only used for serving assets.

"""


def init_app(app, **kwargs):
    """ Performs app-initialization operations related to the current extension. """
    app.extensions['webpack'] = {'assets': None, }

    # Registers context processors
    from . import context_processors
    app.context_processor(context_processors.webpack_assets)
