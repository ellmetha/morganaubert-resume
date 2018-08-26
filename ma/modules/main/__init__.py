"""
    The main module
    ===============

    This module defines - among other things - the generic views and error handlers that should be
    present in most of web applications.

"""


def init_app(app, **kwargs):
    """ Performs app-initialization operations related to the current module. """
    # Registers error handlers.
    from . import errors  # noqa: F401

    # Registers blueprints.
    from . import views
    app.register_blueprint(views.main_blueprint)
