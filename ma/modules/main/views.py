"""
    Main views
    ==========

    This module defines generic views that should be present in most of web applications.

"""

from flask import Blueprint, render_template


main_blueprint = Blueprint('main', __name__)


@main_blueprint.route('/robots.txt', methods=['GET', ])
def robots():
    """ Renders the standard robots.txt file. """
    return render_template('robots.txt')
