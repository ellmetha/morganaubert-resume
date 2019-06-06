"""
    The resume module
    =================

    This module defines - among other things - the views responsible for exposing personal
    information.

"""


def init_app(app, **kwargs):
    """ Performs app-initialization operations related to the current module. """
    # Registers blueprints.
    from . import views
    app.register_blueprint(views.resume_blueprint)

    # Registers context processors
    from . import context_processors
    app.context_processor(context_processors.google_metadata)
