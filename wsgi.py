#!/usr/bin/env python

"""
    The autoapp module
    ==================

    This module creates an instance of the Flask application.

"""

import os

from main import create_app


application = app = create_app(os.getenv('FLASK_CONFIG', 'default'))
