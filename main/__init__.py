from flask import Flask, redirect, request

from config import config

from . import extensions, modules


def create_app(config_name):
    config_obj = config[config_name]()
    app = Flask(__name__, static_url_path='/static')

    # Initializes configuration values.
    app.config.from_object(config_obj)

    # Configure SSL if the current platform supports it.
    if not app.debug and not app.testing and not app.config.get('SSL_DISABLE'):
        from flask_sslify import SSLify
        SSLify(app)

    @app.before_request
    def redirect_www():
        """ Redirects www requests to non-www. """
        if request.host.startswith('www.'):
            new_host = request.host[4:]
            return redirect(f"{request.scheme}://{new_host}/", code=301)

    # Initializes Flask extensions.
    extensions.init_app(app)

    # Initializes modules.
    modules.init_app(app)

    return app
