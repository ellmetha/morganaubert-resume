"""
    Extensions setup
    ================

    Extensions can be used to provide access to common resources of the application. New extension
    instantiations and initializations should be done in this package.

"""

from flask_babel import Babel
from flask_debugtoolbar import DebugToolbarExtension

from . import assets


babel = Babel()
debug_toolbar = DebugToolbarExtension()


def init_app(app):
    """ Initializes the extensions of the application. """
    for extension in (babel, assets, ):
        extension.init_app(app)

    # Initializes development extensions if applicable
    if app.debug:
        for extension in (debug_toolbar, ):
            extension.init_app(app)
