"""
    The dev module
    ==============

    This module defines context processors and views that are only used during developments.

"""


def init_app(app, **kwargs):
    """ Performs app-initialization operations related to the current module. """
    # Registers context processors
    from . import context_processors
    app.context_processor(context_processors.webpack)
